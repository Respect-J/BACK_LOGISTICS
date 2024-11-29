from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.crypto import get_random_string

class User(AbstractUser):
    CLIENT = 1
    SALESPERSON = 2
    LOGISTICIAN = 3

    ROLE_CHOICES = (
        (CLIENT, 'Client'),
        (SALESPERSON, 'Salesperson'),
        (LOGISTICIAN, 'Logistician'),
    )

    # Замена стандартного автоинкрементного ID на собственное поле
    id = models.CharField(max_length=6, unique=True, primary_key=True, editable=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CLIENT)
    email = models.EmailField(unique=True)

    last_name = models.CharField(max_length=150, blank=True)
    verification_code = models.CharField(max_length=5, blank=True, null=True)  # Поле для кода

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_unique_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id():
        while True:
            new_id = get_random_string(length=6, allowed_chars='0123456789')
            if not User.objects.filter(id=new_id).exists():
                return new_id

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
