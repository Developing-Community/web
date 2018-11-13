from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework import serializers

from .models import Content


class ContentCreateSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    subject = serializers.CharField(max_length=255)

    class Meta:
        model = Content
        fields = [
            'title',
            'type',
            'visibility',
            'subject',
            'image',
            'content',
            'draft',
            'publish',
        ]


class ContentSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'pk',
            'title',
            'type',
            'visibility',
            'author',
            'slug',
            'image',
            'height_field',
            'width_field',
            'content',
            'draft',
            'publish',
            'updated',
            'timestamp',
            'up_voters',
            'down_voters'
        ]
        read_only_fields = (
            'pk',
            'author',
            'slug',
            'timestamp',
            'height_field',
            'width_field'
            , 'up_voters',
            'down_voters')
