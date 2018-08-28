from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model



from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


User = get_user_model()

#
# class UserDetailSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'first_name',
#             'last_name',
#         ]




class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')

    def __init__(self, *args, **kwargs):
        super(UserCreateSerializer, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
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
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



# class UserLoginSerializer(ModelSerializer):
#     token = CharField(allow_blank=True, read_only=True)
#     username = CharField()
#     email = EmailField(label='Email Address')
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'token',
#
#         ]
#         extra_kwargs = {"password":
#                             {"write_only": True}
#                             }
#     def validate(self, data):
#         # email = data['email']
#         # user_qs = User.objects.filter(email=email)
#         # if user_qs.exists():
#         #     raise ValidationError("This user has already registered.")
#         return data


