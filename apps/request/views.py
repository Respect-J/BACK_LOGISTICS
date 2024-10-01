from tkinter import SINGLE
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Request
from .serializers import CargoRequestSerializers, SearchRequestSerializers, SimpleRequestSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]  # Требуется авторизация
    queryset = Request.objects.all()
    
    
    def get_serializer_class(self):
        request_type = self.request.query_params.get('request_type')  # Получаем тип из параметров запроса
        if request_type == 'cargo':
            return CargoRequestSerializers
        elif request_type == 'simple':
            return SimpleRequestSerializers
        elif request_type == 'search':
            return SearchRequestSerializers
        return None
    
    
    def perform_create(self, serializer):
        # Изменяем значение request_type перед сохранением
        request_type = self.request.data.get('request_type')
        if request_type in [CARGO, SIMPLE, SEARCH]:            # type: ignore
            serializer.validated_data['request_type'] = request_type
        else:
            serializer.validated_data['request_type'] = SIMPLE # type: ignore # Значение по умолчанию или другое
        
        # Сохраняем объект с указанным пользователем
        serializer.save(user=self.request.user)
    
    
    # POST обработка
    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        if not serializer_class:
            return Response({"error": "Invalid request type."}, status=status.HTTP_400_BAD_REQUEST)

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
        # Получаем объект заявки по ID
        request_instance = self.get_object()
        serializer = self.get_serializer(request_instance)
        
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