from django.db import models
from models import BaseModel


class Contacts(BaseModel):
    first_contact = models.CharField(max_length=256, null=True, blank=True)
    second_contact = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.first_contact


class Banners(BaseModel):
    main_title = models.CharField(max_length=256, null=True, blank=True)
    second_title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="img/banners/")

    def __str__(self):
        return self.main_title


class Docs(BaseModel):
    main_title = models.CharField(max_length=256, null=True, blank=True)
    docs = models.FileField(upload_to="docs/")

    def __str__(self):
        return self.main_title

