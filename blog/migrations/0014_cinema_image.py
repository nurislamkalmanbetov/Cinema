# Generated by Django 4.1.7 on 2023-03-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_job_title_jobtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
