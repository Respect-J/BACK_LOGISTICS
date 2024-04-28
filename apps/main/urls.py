from django.urls import path

from .views import BannersView, DocsView, ContactsView

urlpatterns = [
    path('banners/', BannersView.as_view(), name="banner-get"),
    path('docs/', DocsView.as_view(), name="docs-get"),
    path('contacts/', ContactsView.as_view(), name="contacts-get")


]