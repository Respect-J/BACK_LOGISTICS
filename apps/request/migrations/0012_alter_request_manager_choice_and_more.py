# Generated by Django 5.0.3 on 2024-10-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0011_alter_request_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='manager_choice',
            field=models.CharField(choices=[('salesperson', 'Продавец'), ('logistician', 'Логист')], max_length=255),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.CharField(choices=[('cargo', 'Запрос на карго'), ('simple', 'Простая заявка'), ('search', 'Запрос на поиск')], max_length=16),
        ),
        migrations.AlterField(
            model_name='request',
            name='service_choice',
            field=models.CharField(choices=[('deliveryfromchina', 'Доставка из китая')], max_length=255),
        ),
    ]