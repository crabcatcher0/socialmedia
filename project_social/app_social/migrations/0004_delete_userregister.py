# Generated by Django 5.0.1 on 2024-01-29 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0003_alter_userregister_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]
