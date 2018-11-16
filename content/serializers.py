from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework import serializers

from users.serializers import ProfileRetrieveUpdateSerializer
from .models import Content


class ContentCreateSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'title',
            'type',
            'visibility',
            'image',
            'content',
            'draft',
            'publish',
        ]


class ContentSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    author = ProfileRetrieveUpdateSerializer()

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
            'down_voters',
            'answers',
            'comments',
            'replies',
        ]
        read_only_fields = [
            'pk',
            'author',
            'slug',
            'timestamp',
            'height_field',
            'width_field',
            'up_voters',
            'down_voters',
            'answers',
            'comments',
            'replies',
        ]

    def get_fields(self):
        fields = super(ContentSerializer, self).get_fields()
        fields['answers'] = ContentSerializer(many=True)
        fields['comments'] = ContentSerializer(many=True)
        fields['replies'] = ContentSerializer(many=True)
        return fields
