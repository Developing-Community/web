# Generated by Django 2.0.7 on 2018-09-19 05:56

import content.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20180919_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='main_type',
            field=enumfields.fields.EnumField(default='TEXT', enum=content.models.MainContentType, max_length=1),
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=enumfields.fields.EnumField(default='ARTICLE', enum=content.models.ContentType, max_length=1),
        ),
        migrations.AddField(
            model_name='content',
            name='visibility',
            field=enumfields.fields.EnumField(default='PUBLIC', enum=content.models.ContentVisibility, max_length=1),
        ),
    ]
