from django.db import models
from apps.users.models import User
from models import BaseModel


class Request(BaseModel):
    
    CARGO = 'catgo'
    SIMPLE = 'simple'
    SEARCH = 'search'
    
    PEQUEST_TYPE_CHOICES = [
        (CARGO, 'Запрос на карго'),
        (SIMPLE, 'Простая заявка'),
        (SEARCH, 'Запрос на поиск')
        
    ]

    #привязка заявки к пользователю
    user = models.ForeignKey( User,
                             on_delete=models.CASCADE,
                             related_name='requests'
                             )
    
    
    #имя клиента заявки
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False
                            )
    
    
    #контактный номер заявки
    phone = models.CharField(max_length=20,
                             null=False,
                             blank=False
                             )
    
    
    #контактный email заявки
    email = models.EmailField(null=False,
                              blank=False
                              )
    
    
    #тип запроса/заявки...
    request_type = models.CharField( max_length=16,
                                    choices= PEQUEST_TYPE_CHOICES,
                                    null=False
                                    )
    
    
    #комментарий к запросу/заявке (карго/простая/поиск)
    comment = models.TextField( max_length=1000,
                               null=True,
                               blank=True
                               )
    
    
    #прикрепленный файл/документ (карго/простая/поиск)
    document = models.FileField( upload_to='documents/',
                                null=True,
                                blank=True
                                )
    
    
    #выбор менеджера заявки (карго/простая/поиск)
    manager_chice = models.CharField( max_length=255,
                                    null=False,
                                    default="manager1"
                                    )
    
    
    #поиск товара по имени/названию
    search_item = models.TextField(null=False, 
                                   default='search_item'
                                   )
    
    
    #желаемая цена за единицу (шт)
    desire_price = models.DecimalField( max_digits=10,
                                       decimal_places=2,
                                       null=False,
                                       default=0.0
                                       )
    
    
    #количество
    quantity = models.IntegerField( default=1,
                                   null=True,
                                   blank=True
                                   )
    
    
    #ссылка на товар
    search_link = models.URLField(max_length=200,
                                  blank=True,
                                  null=True
                                  )
    
    #дополнительная информация (карго/поиск)
    additional_information = models.TextField(max_length=1000,
                                              null=True,
                                              blank=True
                                              )
    
    
    #выбор услуши для простой заявки
    service_choice = models.CharField( max_length=255,
                                    null=False,
                                    default='default_service'
                                    )
    
    
    
    def __str__(self):
        return f"Request from {self.name} ({self.email}) - {self.get_request_type_display()}"
    
    