from django.contrib.auth import (
    get_user_model,
)
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.reverse import reverse,reverse_lazy

from .permissions import IsOwner
from .models import Profile
from .serializers import (
    UserCreateSerializer,
    ProfileRetrieveUpdateSerializer,
    ProfileImageUpdateRetriveSerializer)
from django.http import HttpResponseRedirect
User = get_user_model()

class ProfileImageAPIView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileImageUpdateRetriveSerializer
    parser_classes = [MultiPartParser]
    
    def get(self, request, pk,format=None):
        profile = Profile.objects.filter(user__pk=pk).first()
        return Response(ProfileImageUpdateRetriveSerializer(profile).data)
    
    def put(self,request,pk,format=None):
        profile = Profile.objects.filter(user=self.request.user).first()
        profile.profile_image = request.data['profile_image']
        profile.save()
        return Response(ProfileImageUpdateRetriveSerializer(profile).data)
    def delete(self,request,pk,format=None):
        profile = Profile.objects.filter(user=self.request.user).first()
        profile.delete()
        return Response({"status":"Profile Image Removed"})

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
