# Generated by Django 4.2.7 on 2024-03-10 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0002_reportdefinition_reportrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReportDefinition',
        ),
        migrations.DeleteModel(
            name='ReportRequest',
        ),
    ]
