from django.contrib.auth.hashers import make_password
from django.db import models

from models import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=256, null=True, blank=True)
    mainimg = models.ImageField(upload_to="users/", null=True, blank=True)
    password = models.CharField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None