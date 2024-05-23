from rest_framework import generics
from .models import Banners, Docs, Contacts, TypeDelivery, Directions, DeliveryFromChina, Advantages
from .serializers import BannersSerializer, DocsSerializer, ContactsSerializer, TypeDeliverySerializer, \
    DirectionsSerializer, DeliveryChinaSerializer, AdvantagesSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class BannersView(generics.ListAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer


class DocsView(generics.ListAPIView):
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer


class ContactsView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class TypeDeliveryView(generics.ListAPIView):
    queryset = TypeDelivery.objects.all()
    serializer_class = TypeDeliverySerializer


class DirectionsView(generics.ListAPIView):
    queryset = Directions.objects.all()
    serializer_class = DirectionsSerializer


class DeliveryFromChinaView(generics.ListAPIView):
    queryset = DeliveryFromChina.objects.all()
    serializer_class = DeliveryChinaSerializer


class AdvantagesView(generics.ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
