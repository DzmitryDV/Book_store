# Generated by Django 4.1.2 on 2022-10-10 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0006_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='description',
            field=models.CharField(default='Белорусский рубль', max_length=40),
        ),
    ]
