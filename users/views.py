from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .permissions import IsOwner
from .serializers import ProfileRetrieveUpdateSerializer, UserCreateSerializer


from django.urls import reverse
# from django.template.loader import render_to_string

from django.core.mail import send_mail

@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    rest_url = reverse("user:reset_password",kwargs={'key':reset_password_token.key})
    print("INFO:" + rest_url)
    title = "Password Reset Request For " + "\"" + reset_password_token.user.username +"\""
    content = rest_url
    mail_data = {
        
        
        "from" : "noreplay@dev-community.ir",
        "to": ['snparvizi75@gmail.com']
        }
    send_mail(**mail_data,fail_silently=False)
    return HttpResponse("cuker")

def reset_password_change(request,key):
    return HttpResponse(request.get_full_path())

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
