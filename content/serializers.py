from rest_framework import serializers
from .models import Content
class ContentCreateSerializer(serializers.ModelSerializer):
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
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'pk',
            'title',
            'type',
            'visibility',
            'author',
            'slug',
            'subject',
            'image',
            'height_field',
            'width_field',
            'content',
            'draft',
            'publish',
            'updated',
            'timestamp',
            'terms',
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
            ,'up_voters',
            'down_voters',
            'terms')