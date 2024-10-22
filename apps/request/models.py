from django.db import models
from apps.users.models import User
from models import BaseModel

class RequestType(models.TextChoices):
    CARGO = 'cargo', 'Запрос на карго'
    SIMPLE = 'simple', 'Простая заявка'
    SEARCH = 'search', 'Запрос на поиск'
    
class ManagerChice(models.TextChoices):
    SALESPERSON = 'salesperson', 'Продавец'
    LOGISTICIAN = 'logistician', 'Логист'
    
class StatusChoice(models.TextChoices):
    STATUS_NEW = 'new', 'Новый'
    STATUS_IN_PROGRESS = 'in_progress', 'В процессе'
    STATUS_COMPLETED = 'completed', 'Завершен'
    STATUS_CANCELED = 'canceled', 'Отклонен'
    
class ServisChoice(models.TextChoices):
    DELIVERY_FROM_CHINA = 'deliveryfromchina', 'Доставка из китая'


class Request(BaseModel):

    status = models.CharField(
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.STATUS_NEW,
    )
    
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
                                    choices=RequestType.choices,
                                    null=False,
                                    blank=False
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
    manager_choice = models.CharField( max_length=255,
                                    choices=ManagerChice.choices,
                                    null=False,
                                    blank=False
                                    )
    
    
    #поиск товара по имени/названию
    search_item = models.TextField(null=False,
                                   blank=False,
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
                                   )
    
    
    #ссылка на товар
    search_link = models.URLField(max_length=200,
                                  blank=True,
                                  null=True
                                  )

    
    #выбор услуши для простой заявки
    service_choice = models.CharField( max_length=255,
                                      choices=ServisChoice.choices,
                                    null=False,
                                    blank=False
                                    )
    
    
    
    def __str__(self):
        return f"Request from {self.name} ({self.email}) - {self.get_request_type_display()}"
    
    