from rest_framework import serializers

from .models import Banners, Docs, Contacts, TypeDelivery, Advantages, DeliveryFromChina, Directions


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


class DeliveryChinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFromChina
        fields = ["main_title", "second_title", "description", "img"]


class DirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directions
        fields = ["main_title", "description", "img"]


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ["main_title", "second_title", "description", "img"]


class TypeDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDelivery
        fields = ["main_title", "description", "img"]
