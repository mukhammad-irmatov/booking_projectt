# Generated by Django 4.1.2 on 2022-10-11 08:40

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phone_field.models.PhoneField(default='94', help_text='Contact phone number', max_length=9, unique=True),
        ),
    ]
