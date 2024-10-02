from django.urls import path
from .views import RequestDetailView

urlpatterns = [
    path('requests/', RequestDetailView.as_view(), name='request-list_post'), # получить список всех запросов без фильтрации + POST обработка
    path('requests/<uuid:id>/', RequestDetailView.as_view(), name='request-list'),  # GET для конкретной заявки с поиском по ID
    path('requests/<uuid:id>/', RequestDetailView.as_view(), name='request-detail'),  # GET, PUT, PATCH, DELETE для обновления
]