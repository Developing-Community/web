# Generated by Django 2.0.7 on 2018-09-14 08:33

import campaigns.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_auto_20180914_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignpartyrelation',
            name='type',
            field=enumfields.fields.EnumField(enum=campaigns.models.CampaignPartyRelationType, max_length=10),
        ),
        migrations.AlterField(
            model_name='campaigntermrelation',
            name='type',
            field=enumfields.fields.EnumField(enum=campaigns.models.CampaignTermRealtionType, max_length=10),
        ),
    ]
