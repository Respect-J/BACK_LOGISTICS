from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Request
from .serializers import CargoRequestSerializers, SearchRequestSerializers, SimpleRequestSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from apps.users.models import User
from django.utils.dateparse import parse_date






class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Требуется авторизация
    queryset = Request.objects.all()
    lookup_field = 'id'

    # метод для получения сериализаторов по типу запроса
    def get_serializer_class(self):

        if self.request.method == 'GET' or self.request.method == 'PATCH':
            request_id = self.kwargs.get('id', None) 
        

            if request_id is not None:
                request_instance = get_object_or_404(Request, id=request_id)
                request_type = request_instance.request_type
            else:

                queryset = self.filter_queryset(self.get_queryset())
                if not queryset.exists():
                    raise ValidationError("No requests found for given filters")


                request_instance = queryset.first()
                request_type = request_instance.request_type
            
        else:
            request_type = self.request.data.get('request_type')

        serializers_map = {
            'cargo': CargoRequestSerializers,
            'simple': SimpleRequestSerializers,
            'search': SearchRequestSerializers
        }


        serializer_class = serializers_map.get(request_type)
    
        if serializer_class is not None:
            return serializer_class

        
        raise ValidationError(f"Unknown request type: {request_type}")

    # предварительные проверки перед сохранением 
    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated:
            raise ValueError("User is not authenticated.")
        
        if not isinstance(user, User):
            raise ValueError(f"Request.user must be a User instance.")

        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return Request.objects.all()
    
    
    
    
    
    # POST обработка
    def post(self, request, *args, **kwargs):
        
        serializer_class = self.get_serializer_class()
        
        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)

        if not request.user.is_authenticated:
            return Response({"error": "User must be authenticated."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            
            return Response({
                "message": "Request created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "There were errors with your request.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
        
        
    
    # GET обработка
    def get(self, request, *args, **kwargs):
        request_id = kwargs.get('id', None)
        
        if request_id is not None:
            request_instance = get_object_or_404(Request, id=request_id)
            serializer = self.get_serializer(request_instance)
            return Response(serializer.data)

        else:
            date_from = request.query_params.get('date_from', None)
            date_to = request.query_params.get('date_to', None)
            status = request.query_params.get('status', None)

            if not date_from and not date_to and not status:
                return Response({"detail": "At least one filter (date_from, date_to, status) is required"}, status=400)

            queryset = self.get_queryset()

            if date_from:
                date_from = parse_date(date_from)
                if not date_from:
                    return Response({"detail": "Invalid date format for date_from"}, status=400)
                queryset = queryset.filter(created_at__gte=date_from)

            if date_to:
                date_to = parse_date(date_to)
                if not date_to:
                    return Response({"detail": "Invalid date format for date_to"}, status=400)
                queryset = queryset.filter(created_at__lte=date_to)

            if status:
                queryset = queryset.filter(status=status)

            if not queryset.exists():
                return Response({"detail": "No requests found for these filters"}, status=404)

            serializer_class = self.get_serializer_class()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data)
            
    
    
    
    # PUT обработка
    def put(self, request, *args, **kwargs):

        request_instance = self.get_object()
        serializer_class = self.get_serializer_class()

        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(request_instance, data=request.data)

        if serializer.is_valid():

            self.perform_update(serializer)
            return Response({
                "message": "Request updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "There were errors with your request.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    # PATCH обработка
    def patch(self, request, *args, **kwargs):

        request_instance = self.get_object()  


        serializer_class = self.get_serializer_class()
        serializer = serializer_class(request_instance, data=request.data, partial=True)


        if serializer.is_valid():

            self.perform_update(serializer)
            return Response({
                "message": "Request partially updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "There were errors with your request.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    
    
    # DELETE обработка
    def delete(self, request, *args, **kwargs):
        # Удаление заявки
        request_instance = self.get_object()
        request_instance.delete()
        return Response({"message": "Request deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    