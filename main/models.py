from django.db import models
from models import BaseModel


class Contacts(BaseModel):
    first_contact = models.CharField(max_length=256)
    second_contact = models.CharField(max_length=256)

    def __str__(self):
        return self.first_contact


class Banner(BaseModel):
    main_title = models.CharField(max_length=256)
    second_title = models.CharField(max_length=256)
    description = models.TextField()
    img = models.ImageField(upload_to="img/banners/")

    def __str__(self):
        return self.main_title
