from rest_framework import serializers

from .models import Banners, Docs, Contacts


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ["main_title", "second_title", "description", "img"]


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ["main_title", "docs"]


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ["first_contact", "second_contact"]

