import random
from django.contrib.auth.models import AbstractUser
from django.db import models


def generate_unique_id():
    while True:
        unique_id = random.randint(1000000, 9999999)
        if not CustomUser.objects.filter(id=unique_id).exists():
            return unique_id


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', 'Regular User'),
        ('logistics', 'Logistics Manager'),
        ('sales', 'Sales Manager'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='regular')
    id = models.IntegerField(primary_key=True, default=generate_unique_id, editable=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_id()
        super().save(*args, **kwargs)

    def clean(self):
        if not (1000000 <= self.id <= 9999999):
            raise ValidationError('ID должен быть 7-значным числом.')
