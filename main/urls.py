from django.urls import path

from .views import BannerListCreateView, BannerRetrieveUpdateDestroyView

urlpatterns = [
    path("", BannerListCreateView.as_view(), name="banner-get-create"),
    path("<pk>/", BannerRetrieveUpdateDestroyView.as_view(), name="banner-retrieve-update-destroy"),

]