# Generated by Django 5.0.3 on 2024-10-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_alter_request_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='additional_information',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='desire_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='request',
            name='manager_chice',
            field=models.CharField(default='manager1', max_length=255),
        ),
        migrations.AlterField(
            model_name='request',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='search_item',
            field=models.TextField(default='search_item'),
        ),
        migrations.AlterField(
            model_name='request',
            name='service_choice',
            field=models.CharField(default='default_service', max_length=255),
        ),
    ]