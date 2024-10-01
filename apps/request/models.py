from django.db import models
from apps.users.models import User
import uuid

class Request(models.Model):
    
    CARGO = 'catgo'
    SIMPLE = 'simple'
    SEARCH = 'search'
    
    PEQUEST_TYPE_CHOICES = [
        (CARGO, 'Запрос на карго'),
        (SIMPLE, 'Простая заявка'),
        (SEARCH, 'Запрос на поиск')
        
    ]

    #идентификатор для запроса
    id = models.UUIDField( primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )


    #привязка заявки к пользователю
    user = models.ForeignKey( User,
                             on_delete=models.CASCADE,
                             related_name='requests'
                             )
    
    
    #имя клиента заявки
    name = models.CharField(max_length=255)
    
    
    #контактный номер заявки
    phone = models.CharField(max_length=20)
    
    
    #контактный email заявки
    email = models.EmailField()
    
    
    #тип запроса/заявки...
    request_type = models.CharField( max_length=10,
                                    choices= PEQUEST_TYPE_CHOICES,
                                    default= SIMPLE
                                    )
    
    
    #комментарий к запросу/заявке (карго/простая/)
    comment = models.TextField( null=True,
                               blank=True
                               )
    
    
    #прикрепленный файл/документ (карго/простая/поиск)
    document = models.FileField( upload_to='documents/',
                                null=True,
                                blank=True
                                )
    
    
    #выбор менеджера заявки (карго/простая/поиск)
    manager_chice = models.CharField( max_length=255,
                                     null=True,
                                     blank=True
                                     )
    
    
    #дата и время создания/обновления 
    date_created = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    
    #поиск товара по имени/названию
    search_item = models.TextField(null=True,
                                   blank=True
                                   )
    
    
    #желаемая цена за единицу (шт)
    desire_price = models.DecimalField( max_digits=10,
                                       decimal_places=2,
                                       null=True,
                                       blank=True
                                       )
    
    
    #количество
    quantity = models.IntegerField( null=True,
                                   blank=True
                                   )
    
    
    #ссылка на товар
    search_link = models.URLField(max_length=200,
                                  blank=True,
                                  null=True
                                  )
    
    #дополнительная информация (карго/поиск)
    additional_information = models.TextField( null=True,
                                              blank=True
                                              )
    
    
    #выбор услуши для простой заявки
    service_choice = models.CharField( max_length=255,
                                     null=True,
                                     blank=True
                                     )
    
    
    
    def __str__(self):
        return f"Request from {self.name} ({self.email}) - {self.get_request_type_display()}"
    
    