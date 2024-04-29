from django.urls import path

from .views import BannersView, DocsView, ContactsView, DirectionsView, AdvantagesView, TypeDeliveryView,\
    DeliveryFromChinaView

urlpatterns = [
    path('banners/', BannersView.as_view(), name="banner-get"),
    path('docs/', DocsView.as_view(), name="docs-get"),
    path('contacts/', ContactsView.as_view(), name="contacts-get"),
    path('directions/', DirectionsView.as_view(), name="directions-get"),
    path('advantages/', AdvantagesView.as_view(), name="advantages-get"),
    path('delivery/', TypeDeliveryView.as_view(), name="delivery-get"),
    path('china/', DeliveryFromChinaView.as_view(), name="china-get")


]