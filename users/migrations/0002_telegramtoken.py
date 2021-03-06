# Generated by Django 2.0.7 on 2018-09-30 16:11

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramToken',
            fields=[
                ('user_token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('telegram_user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
