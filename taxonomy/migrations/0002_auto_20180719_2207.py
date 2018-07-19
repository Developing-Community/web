# Generated by Django 2.0.6 on 2018-07-19 22:07

from django.db import migrations, models
import django.db.models.deletion
import taxonomy.models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(taxonomy.models.TermRealtionType('child_of'), 'child_of')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='term',
            name='parent',
        ),
        migrations.AddField(
            model_name='termrelation',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='taxonomy.Term'),
        ),
        migrations.AddField(
            model_name='termrelation',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='taxonomy.Term'),
        ),
    ]