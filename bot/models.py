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
    LOGIN_PASSWORD = "LOGIN_PASSWORD"
    REGISTER = "REGISTER"
    REGISTER_USERNAME = "REGISTER_USERNAME"
    REGISTER_PASSWORD = "REGISTER_PASSWORD"
    ADD_PROJECT_JOB = "ADD_PROJECT_JOB"
    ADD_PROJECT_JOB_SKILLS = "ADD_PROJECT_JOB_SKILLS"
    EDIT_PROFILE = "EDIT_PROFILE"
    EDIT_PROFILE_NAME = "EDIT_PROFILE_NAME"
    EDIT_PROFILE_BIO = "EDIT_PROFILE_BIO"
    EDIT_PROFILE_SKILLS = "EDIT_PROFILE_SKILLS"

class TelegramUserInputKeys(Enum):
    USERNAME_OR_EMAIL = 'USERNAME_OR_EMAIL'
    USERNAME = 'USERNAME'
    EMAIL = 'EMAIL'
    PROJECT_CONTENT = 'PROJECT_CONTENT'


class TelegramUserInput(models.Model):
    key = EnumField(TelegramUserInputKeys, max_length=1000)
    value = models.TextField()


class TelegramProfile(models.Model):
    telegram_user_id = models.IntegerField(primary_key=True, unique=True)
    profile = models.ForeignKey(Profile, related_name="telegram_profile", null=True, blank=True,
                                on_delete=models.CASCADE)
    verify_token = models.UUIDField(default=uuid.uuid4, editable=False)
    menu_state = EnumField(MenuState, default=MenuState.START, max_length=1000)
    user_input = models.ManyToManyField(to=TelegramUserInput, related_name='user_input', blank=False)
