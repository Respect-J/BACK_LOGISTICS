from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestDetailView

router = DefaultRouter()

router.register(r'requests', RequestDetailView, basename='request')

urlpatterns = [
    path('request_filter_post/', RequestDetailView.as_view({'post': 'create', 'get': 'list'}), name='request-filter_post'), # Обработка GET и POST
    path('requests/<uuid:pk>/', RequestDetailView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='request-detail'), # GET, PUT, PATCH, DELETE для обновления
    # path('', include(router.urls)),  # Включаем маршруты из маршрутизатора
]