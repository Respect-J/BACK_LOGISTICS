from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Поля, отображаемые при редактировании пользователя
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

    # Поля, отображаемые при добавлении нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )

    # Добавляем фильтрацию по роли
    list_filter = UserAdmin.list_filter + ('role',)
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')

    # Возможность редактировать роль в списке
    list_editable = ('role',)

admin.site.register(User, CustomUserAdmin)
