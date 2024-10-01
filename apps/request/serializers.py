from rest_framework import serializers
from .models import Request



class CargoRequestSerializers(serializers.ModelSerializers):
    
    user = serializers.ReadOnlyField(source='user.username')  # Поле для отображения пользователя
    
    class Meta:
        model = Request
        fields = ['id',
                  'request_type',
                  'name',
                  'phone',
                  'email',
                  'comment',
                  'document',
                  'manager_choice',
                  'user'
                  ]


class SearchRequestSerializers(serializers.ModelSerializers):
    
    user = serializers.ReadOnlyField(source='user.username')  
    
    class Meta:
        model = Request
        fields = ['id',
                  'request_type',
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
        
        
class SimpleRequestSerializers(serializers.ModelSerializers):
    
    user = serializers.ReadOnlyField(source='user.username')  
    
    class Meta:
        model = Request
        fields = ['id',
                  'request_type',
                  'name',
                  'phone',
                  'email',
                  'service_choice',
                  'comment',
                  'document',
                  'manager_chice',
                  'user'
                  ]