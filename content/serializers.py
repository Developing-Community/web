from rest_framework import serializers
from .models import Content
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