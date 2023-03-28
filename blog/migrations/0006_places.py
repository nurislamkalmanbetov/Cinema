# Generated by Django 4.1.7 on 2023-03-27 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_seanses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.IntegerField(verbose_name='Номер ряда')),
                ('row_place', models.IntegerField(verbose_name='Номер места')),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='blog.saloon', verbose_name='Места')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['places'],
            },
        ),
    ]
