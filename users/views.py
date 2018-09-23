from django.http import HttpResponse

import requests
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

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
from django.shortcuts import render
from .models import Profile
from .permissions import IsOwner
from .serializers import ProfileRetrieveUpdateSerializer, UserCreateSerializer

from django.conf import settings
#`current_user`, `username`, `email`, `reset_password_url`

def get_http_host(request):
    return HttpResponse("{}".format(request.META['HTTP_HOST']))

@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    reset_url = reverse("user:reset_password",kwargs={'key':reset_password_token.key})
    reset_link = settings.HTTP_HOST + reset_url
    print("INFO:" + reset_link)
    context = {
    'current_user': reset_password_token.user,
    'username': reset_password_token.user.username,
    'email': reset_password_token.user.email,
    'reset_link': reset_link
    }
    title = "Password Reset Request For " + "\"" + reset_password_token.user.username +"\""
    content_html = render_to_string("email/reset_password_email.html",context)
    content_text = strip_tags(content_html)
    mail_from = "noreply@dev-community.ir"
    to = ['snparvizi75@gmail.com']

    email = EmailMultiAlternatives(
        title,
        content_text,
        mail_from,
        to)
    email.attach_alternative(content_html,"text/html")
    email.send()

def reset_password_change(request,key):
    context = {
        'key': key,

    }
    return render(request,"email/reset_password.html",context)

# from django.core.mail import get_connection, EmailMultiAlternatives

# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender:
#     :param reset_password_token:
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#     'current_user': reset_password_token.user,
#     'username': reset_password_token.user.username,
#     'email': reset_password_token.user.email,
#     # ToDo: The URL can (and should) be constructed using pythons built-in `reverse` method.
#     'reset_password_url': "http://some_url/reset/?token={token}".format(token=reset_password_token.key)
#     }

#     # render email text
#     email_html_message = render_to_string('email/reset_password.html', context)
#     email_plaintext_message = render_to_string('email/reset_password.txt', context)

#     msg = EmailMultiAlternatives(
#     # title:
#     ("Password Reset for {title}".format(title="Some website title")),
#     # message:
#     email_plaintext_message,
#     # from:
#     "noreply@somehost.local",
#     # to:
#     [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()





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
