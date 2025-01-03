from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'request_type', 'created_at', 'status')
    search_fields = ('name', 'email')
    list_filter = ('request_type', 'created_at', 'status')  


admin.site.register(Request, RequestAdmin)

