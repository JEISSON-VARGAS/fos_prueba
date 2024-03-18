# Generated by Django 4.2.7 on 2024-03-13 21:32

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_alter_sale_discount_alter_sale_vat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fabrication_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 3, 13))], verbose_name='Fecha Fabricación'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 3, 13))], verbose_name='Fecha Venta'),
        ),
    ]
