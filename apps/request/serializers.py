from rest_framework import serializers
from .models import Request



class CargoRequestSerializers(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')  # Поле для отображения пользователя
    
    class Meta:
        model = Request
        fields = ['id',
                  'request_type',
                  'status',
                  'name',
                  'phone',
                  'email',
                  'comment',
                  'document',
                  'manager_choice',
                  'user'
                  ]
        read_only_fields = ['id','user']

class SearchRequestSerializers(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')  
    
    class Meta:
        model = Request
        fields = ['id',
                  'request_type',
                  'status',
                  'name',
                  'phone',
                  'email',
                  'search_item',
                  'desire_price',
                  'quantity',
                  'document',
                  'search_link',
                  'comment',
                  'manager_choice',
                  'user'
                  ]
        read_only_fields = ['id','user']

        
        
class SimpleRequestSerializers(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')  
    
    class Meta:
        model = Request
        fields = ['id',
                  'request_type',
                  'status',
                  'name',
                  'phone',
                  'email',
                  'service_choice',
                  'comment',
                  'document',
                  'manager_choice',
                  'user'
                  ]
        read_only_fields = ['id','user']

        