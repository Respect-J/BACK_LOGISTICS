from rest_framework import status
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from .models import Request
from .serializers import CargoRequestSerializers, SearchRequestSerializers, SimpleRequestSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.utils.dateparse import parse_date
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi






class RequestDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]  # Требуется авторизация
    queryset = Request.objects.all()
    lookup_field = 'id'

    # метод для получения сериализаторов по типу запроса
    def get_serializer_class(self):

        if self.request.method == 'GET' or self.request.method == 'PATCH':
            request_id = self.kwargs.get('pk', None) 
        

            if request_id is not None:
                request_instance = get_object_or_404(Request, pk=request_id)
                request_type = request_instance.request_type
            else:

                queryset = Request.objects.all()
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

        
        raise ValidationError(f"Неизвестный тип запроса: {request_type}. Доступные типы: {', '.join(serializers_map.keys())}")
    
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Request, pk=pk)
    
    
    
    
    
    
    @swagger_auto_schema(
        operation_description="Создать новый объект",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Ф.И.О.', example='Muhammadyusuf Ismatov'),
                'phone': openapi.Schema(type=openapi.TYPE_INTEGER, description='+998XXXXXXXXX', example='+998991234567'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='name@gmail.com', example='yusuf@gmail.com'),
                'request_type': openapi.Schema(type=openapi.TYPE_STRING, description='simple, cargo, search', example='simple'),
                
            },
            required=['name', 'phone', 'email', 'request_type', ''], 
        ),

    ) # POST обработка
    def create(self, request, *args, **kwargs):
        
        serializer_class = self.get_serializer_class()
        
        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response({
                "message": "Request created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "There were errors with your request.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    
    @swagger_auto_schema(
        operation_description="Получить объект по ID или отфильтровать по дате либо статусу.",
        manual_parameters=[
            openapi.Parameter(
                '<uuid:pk>',
                openapi.IN_QUERY,
                description="Вернуть конкретного пользователя по ID",
                example='.../c55564b0-2edd-4789-86b8-d08c487212b5/',
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'date_from',
                openapi.IN_QUERY,
                description="Дата начала фильтрации в формате YYYY-MM-DD",
                example='.../?date_from=2024-01-01',
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'date_to',
                openapi.IN_QUERY,
                description="Дата окончания фильтрации в формате YYYY-MM-DD",
                example='.../?date_to=2025-12-31',
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'status',
                openapi.IN_QUERY,
                description="Статус запроса для фильтрации",
                example='.../?status=new',
                type=openapi.TYPE_STRING,
            ),
        ]

    ) # GET обработка
    def list(self, request, *args, **kwargs):
        request_id = kwargs.get('pk', None)
        
        if request_id is not None:
            request_instance = get_object_or_404(Request, pk=request_id)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(request_instance)
            return Response(serializer.data)

        else:
            date_from = request.query_params.get('date_from', None)
            date_to = request.query_params.get('date_to', None)
            status = request.query_params.get('status', None)

            if not date_from and not date_to and not status:
                return Response({"detail": "At least one filter (date_from, date_to, status) is required"}, status=400)

            queryset = Request.objects.all()

            if date_from:
                date_from = parse_date(date_from)
                if not date_from:
                    return Response({"detail": "Invalid date format for date_from. Expected format: YYYY-MM-DD"}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                queryset = queryset.filter(created_at__gte=date_from)

            if date_to:
                date_to = parse_date(date_to)
                if not date_to:
                    return Response({"detail": "Invalid date format for date_to. Expected format: YYYY-MM-DD"}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                queryset = queryset.filter(created_at__lte=date_to)

            if status:
                queryset = queryset.filter(status=status)

            if not queryset:
                return Response({"detail": "No requests found for these filters"}, status=404)

            serializer_class = self.get_serializer_class()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data)
    
    
    
    
    
    
    @swagger_auto_schema(
        operation_description="Обновить все поля обьекта по ID",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'request_type': openapi.Schema(type=openapi.TYPE_STRING, description='simple, cargo, search', example='cargo')
            },
            required=['request_type']
        ),

    )   # PUT обработка
    def update(self, request, *args, **kwargs):

        request_instance = self.get_object()
        serializer_class = self.get_serializer_class()

        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(request_instance, data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({
                "message": "Request updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "There were errors with your request.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    @swagger_auto_schema(
        operation_description="Частичное обновление по ID",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'request_type': openapi.Schema(type=openapi.TYPE_STRING, description='simple, cargo, search', example='cargo')
            },
            required=['request_type']
        ),

    )   # PATCH обработка
    def partial_update(self, request, *args, **kwargs):

        request_instance = self.get_object()  


        serializer_class = self.get_serializer_class()
        serializer = serializer_class(request_instance, data=request.data, partial=True)


        if serializer.is_valid():

            serializer.save()
            return Response({
                "message": "Request partially updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        print(serializer.errors)
        return Response({
            "message": "There were errors with your request.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    
    
    
    
    @swagger_auto_schema(
        operation_description="Удалить заявку по ID",

    )  # DELETE обработка
    def destroy(self, request, *args, **kwargs):

        request_instance = self.get_object()
        request_instance.delete()
        return Response({"message": "Request deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    