# Generated by Django 5.1.3 on 2024-12-30 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_otp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='APIKey',
        ),
    ]
