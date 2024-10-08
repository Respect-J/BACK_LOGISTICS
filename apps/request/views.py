from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Request
from .serializers import CargoRequestSerializers, SearchRequestSerializers, SimpleRequestSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication




class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Требуется авторизация
    queryset = Request.objects.all()
    lookup_field = 'id'
    
    
    def get_serializer_class(self):
        request_type = self.request.data.get('request_type')  # Получаем тип из параметров запроса
        
        if request_type == 'cargo':
            return CargoRequestSerializers
        elif request_type == 'simple':
            return SimpleRequestSerializers
        elif request_type == 'search':
            return SearchRequestSerializers
        
        return SimpleRequestSerializers
    
    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated:
            raise ValueError("User is not authenticated.")
        if not isinstance(user, User):  # Замените на вашу модель пользователя
            raise ValueError(f"Request.user must be a User instance.")
        serializer.save(user=user)
    
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
        request_id = kwargs.get('pk', None)

        if request_id is not None:
            request_instance = get_object_or_404(Request, pk=request_id)
            serializer = self.get_serializer(request_instance)
            return Response(serializer.data)

        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class() 
        serializer = serializer_class(queryset, many=True)  # Создаем экземпляр сериализатора
        return Response(serializer.data)
    
    
    
    # PUT обработка
    def put(self, request, *args, **kwargs):
        # Полное обновление заявки
        request_instance = self.get_object()
        serializer_class = self.get_serializer_class()

        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(request_instance, data=request.data)

        if serializer.is_valid():
            # Здесь можно изменить request_type, если это необходимо
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
        # Частичное обновление заявки
        request_instance = self.get_object()
        serializer_class = self.get_serializer_class()

        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)

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