# Generated by Django 2.0.7 on 2018-10-01 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramtoken',
            old_name='user_token',
            new_name='verify_token',
        ),
    ]