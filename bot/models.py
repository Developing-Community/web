from django.db import models

import uuid

from enumfields import Enum, EnumField


# Create your models here.
from web import settings

class TelegramToken(models.Model):
    verify_token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_user_id = models.IntegerField()

class MenuState(Enum):
    START = "START"
    SET_FIRST_NAME = "SET_FIRST_NAME"
    ADD_PROJECT_JOB = "ADD_PROJECT_JOB"

class TelegramProfile(models.Model):
    telegram_user_id = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="telegram_profile", null=True, blank=True, on_delete=models.CASCADE)
    verify_token = models.UUIDField(default=uuid.uuid4, editable=False)
    menu_state = EnumField(MenuState, default= MenuState.START)