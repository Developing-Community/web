# Generated by Django 2.0.6 on 2018-08-10 17:03

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20180810_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='visibility',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE')], default=content.models.ContentVisibility('PUBLIC'), max_length=30),
        ),
    ]