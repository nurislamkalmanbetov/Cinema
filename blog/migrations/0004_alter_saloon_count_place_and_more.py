# Generated by Django 4.1.7 on 2023-03-27 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_saloon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saloon',
            name='count_place',
            field=models.IntegerField(verbose_name='Колличество мест'),
        ),
        migrations.AlterField(
            model_name='saloon',
            name='number_of_places',
            field=models.IntegerField(verbose_name='Число мест'),
        ),
        migrations.AlterField(
            model_name='saloon',
            name='number_of_rows',
            field=models.IntegerField(verbose_name='Число рядов'),
        ),
        migrations.CreateModel(
            name='Sector_salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Секторы зала')),
                ('description', models.CharField(max_length=100, verbose_name='Описание секторов зала')),
                ('sector_salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_salon', to='blog.saloon', verbose_name='Секторы зала')),
            ],
            options={
                'verbose_name': 'Сектор зала',
                'verbose_name_plural': 'Секторы зала',
                'ordering': ['name'],
            },
        ),
    ]
