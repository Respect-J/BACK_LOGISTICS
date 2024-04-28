from rest_framework import generics
from .models import Banners, Docs, Contacts
from .serializers import BannersSerializer, DocsSerializer, ContactsSerializer


class BannersView(generics.ListAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer


class DocsView(generics.ListAPIView):
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer


class ContactsView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
