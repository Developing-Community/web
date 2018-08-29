from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from web.utils import RequiredValidator
from rest_framework.serializers import (
  CharField,
  EmailField,
  HyperlinkedIdentityField,
  ModelSerializer,
  SerializerMethodField,
  ValidationError
)

from users.models import Profile
from campaigns.models import Product

class ProductCreateSerializer(ModelSerializer):

  class Meta:
    model = Product
    fields = [
      'name',
      'description',
      'price'
    ]
