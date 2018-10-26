from django.db import models

import uuid

from enumfields import Enum, EnumField

# Create your models here.
from users.models import Profile
from web import settings


class MenuState(Enum):
    START = "START"
    MAIN = "MAIN"
    LOGIN = "LOGIN"
    REGISTER = "REGISTER"
    SET_FIRST_NAME = "SET_FIRST_NAME"
    ADD_PROJECT_JOB = "ADD_PROJECT_JOB"


class TelegramUserInputKeys(Enum):
    USERNAME_OR_EMAIL = 'USERNAME_OR_EMAIL'
    USERNAME = 'USERNAME'
    EMAIL = 'EMAIL'


class TelegramUserInput(models.Model):
    key = EnumField(TelegramUserInputKeys)
    value = models.TextField()


class TelegramProfile(models.Model):
    telegram_user_id = models.IntegerField(primary_key=True, unique=True)
    profile = models.ForeignKey(Profile, related_name="telegram_profile", null=True, blank=True,
                                on_delete=models.CASCADE)
    verify_token = models.UUIDField(default=uuid.uuid4, editable=False)
    menu_state = EnumField(MenuState, default=MenuState.START)
    user_input = models.ManyToManyField(to=TelegramUserInput, related_name='user_input', blank=False)
