from django.urls import path
from .views import RequestDetailView

urlpatterns = [
    path('requests/', RequestDetailView.as_view(), name='request-list'),  # GET для списка, POST для создания
    path('requests/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),  # GET, PUT, PATCH, DELETE для обновления
]