# Generated by Django 2.0.9 on 2018-10-23 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_profile_telegram_user_id'),
        ('bot', '0005_telegramprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='telegramprofile',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='telegram_profile', to='users.Profile'),
        ),
    ]
