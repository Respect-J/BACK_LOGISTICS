from django.urls import path
from .views import RequestDetailView

urlpatterns = [

    path('request_filter_post/', 
         RequestDetailView.as_view({'post': 'create', 'get': 'list'}), 
         name='request-filter_post'), #фильтрации по датам и статусу + POST обработка

    path('requests/<uuid:pk>/', 
         RequestDetailView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), 
         name='request-detail')  # методы GET, PUT, PATCH, DELETE с указанием ID
]
