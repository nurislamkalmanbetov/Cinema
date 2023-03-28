# Generated by Django 4.1.7 on 2023-03-27 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinema',
            options={'ordering': ['-date_pub'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.RemoveField(
            model_name='cinema',
            name='body',
        ),
        migrations.AddField(
            model_name='cinema',
            name='duration',
            field=models.CharField(default='56', max_length=25, verbose_name='Длительность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema',
            name='name',
            field=models.CharField(default='ff', max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema',
            name='rental_finish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата окончания проката'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema',
            name='rental_start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начало проката'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema',
            name='sales_company',
            field=models.CharField(default='dfghj', max_length=50, verbose_name='Название компании'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cinema',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
    ]
