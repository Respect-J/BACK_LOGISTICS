from django.db import models
from models import BaseModel


class MainModel(BaseModel):
    main_title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Contacts(BaseModel):
    first_contact = models.CharField(max_length=256, null=True, blank=True)
    second_contact = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.first_contact


class Banners(MainModel):
    second_title = models.CharField(max_length=256, null=True, blank=True)
    img = models.ImageField(upload_to="img/banners/")

    def __str__(self):
        return self.main_title


class Docs(MainModel):
    docs = models.FileField(upload_to="docs/")

    def __str__(self):
        return self.main_title


class Directions(MainModel):
    img = models.ImageField(upload_to="img/directions/")

    def __str__(self):
        return self.main_title


class DeliveryFromChina(MainModel):
    second_title = models.CharField(max_length=256, null=True, blank=True)
    img = models.ImageField(upload_to="img/deliveryfromchina/")

    def __str__(self):
        return self.main_title


class TypeDelivery(MainModel):
    img = models.ImageField(upload_to="img/typedelivery/")

    def __str__(self):
        return self.main_title


class Advantages(MainModel):
    second_title = models.CharField(max_length=256, null=True, blank=True)
    img = models.ImageField(upload_to="img/advantages/")

    def __str__(self):
        return self.main_title

