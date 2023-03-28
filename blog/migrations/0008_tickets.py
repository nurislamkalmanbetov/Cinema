# Generated by Django 4.1.7 on 2023-03-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_price_for_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.IntegerField(verbose_name='Номер билета')),
                ('date_created', models.DateTimeField(verbose_name='Дата печати билета')),
                ('payed', models.BooleanField(verbose_name='Оплачено')),
                ('booking', models.BooleanField(verbose_name='Забронирован')),
                ('crashed', models.BooleanField(verbose_name='Утилизирован')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='blog.places', verbose_name='Место')),
                ('seans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seans', to='blog.seanses', verbose_name='Сеанс')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'ordering': ['ticket_number'],
            },
        ),
    ]
