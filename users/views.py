from django.contrib.auth import (
    get_user_model,
)
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwner
from .models import Profile
from .serializers import (
    UserCreateSerializer,
    ProfileRetrieveUpdateSerializer)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class ProfileRetrieveAPIView(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.filter(user=self.request.user).first()
        return Response(ProfileRetrieveUpdateSerializer(profile).data)


class ProfileUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileRetrieveUpdateSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    queryset = Profile.objects.all()
