from django.urls import path
from .views import RequestDetailView

urlpatterns = [
    path('requests/', RequestDetailView.as_view(), name='request-list_post'), # получить список запросов c задаными фильтрациями + POST обработка
    path('requests/<uuid:id>/', RequestDetailView.as_view(), name='request-detail'),  # GET(получить конкретного пользователя), PUT, PATCH, DELETE для обновления
]