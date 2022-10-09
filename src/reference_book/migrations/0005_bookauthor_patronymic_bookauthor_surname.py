# Generated by Django 4.1.2 on 2022-10-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0004_alter_bookauthor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookauthor',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='surname',
            field=models.CharField(default=1, max_length=100, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
