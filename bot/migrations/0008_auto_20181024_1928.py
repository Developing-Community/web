# Generated by Django 2.0.9 on 2018-10-24 19:28

import bot.models
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_delete_telegramtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', enumfields.fields.EnumField(enum=bot.models.TelegramUserInputKeys, max_length=10)),
                ('value', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='telegramprofile',
            name='user_input',
            field=models.ManyToManyField(related_name='user_input', to='bot.TelegramUserInput'),
        ),
    ]
