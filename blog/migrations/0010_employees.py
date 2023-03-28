# Generated by Django 4.1.7 on 2023-03-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_moving_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='ФИО')),
                ('title', models.IntegerField(max_length=255, verbose_name='Информация')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['name'],
            },
        ),
    ]
