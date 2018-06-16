# Generated by Django 2.0.6 on 2018-06-16 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learningFields', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=users.models.profile_image_upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('guiding_fields', models.ManyToManyField(related_name='user_guiding_fields', to='learningFields.LearningField')),
                ('learning_fields', models.ManyToManyField(related_name='user_learning_fields', to='learningFields.LearningField')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
