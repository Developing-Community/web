from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    EmailField,
    ModelSerializer,
    ValidationError
)
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from users.models import Profile

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',

        ]
        extra_kwargs = {"password":
            {
                "write_only": True
            }
        }

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")

        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("ایمیل از قبل وجود دارد")

        return value

    def validate_username(self, value):
        data = self.get_initial()
        username = data.get("username")

        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("نام کاربری از قبل وجود دارد")

        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class ProfileRetrieveUpdateSerializer(ModelSerializer):
    # A thumbnail image, sorl options and read-only
    thumbnail = HyperlinkedSorlImageField(
        '50x50',
        options={"crop": "center"},
        source='profile_image',
        read_only=True
    )

    # A larger version of the image, allows writing
    # profile_image = HyperlinkedSorlImageField('1024')

    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'bio',
            'thumbnail',
            'profile_image',
            'width_field',
            'height_field',
        ]
        read_only_fields = [
            'thumbnail',
            'profile_image',
            'width_field',
            'height_field',
        ]


class ProfileImageUpdateRetriveSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'width_field',
            'height_field',
        ]
        read_only_fields = [
            'width_field',
            'height_field',
        ]
