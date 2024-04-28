from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("", UserListCreateView.as_view(), name="Contact-get-create"),
    path("<pk>/", UserRetrieveUpdateDestroyView.as_view(), name="user-retrieve-update-destroy"),

]