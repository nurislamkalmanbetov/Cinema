# Generated by Django 4.1.7 on 2023-03-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_cinema_options_remove_cinema_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saloon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Залы')),
                ('count_place', models.IntegerField(max_length=200, verbose_name='Колличество мест')),
                ('description', models.CharField(max_length=100, verbose_name='Описание зала')),
                ('number_of_rows', models.IntegerField(max_length=100, verbose_name='Число рядов')),
                ('number_of_places', models.IntegerField(max_length=100, verbose_name='Число мест')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
                'ordering': ['name'],
            },
        ),
    ]