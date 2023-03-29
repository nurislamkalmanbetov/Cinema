# Generated by Django 4.1.7 on 2023-03-27 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_saloon_count_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seanses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seanses', to='blog.cinema', verbose_name='Фильм')),
                ('seanses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seanses', to='blog.saloon', verbose_name='Сеансы')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеансы',
                'ordering': ['movie'],
            },
        ),
    ]