# Generated by Django 4.1.2 on 2022-10-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='BookPublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Издательство')),
            ],
        ),
        migrations.CreateModel(
            name='BookSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Серия')),
            ],
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
    ]
