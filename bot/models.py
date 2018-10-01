from django.db import models

import uuid

class TelegramToken(models.Model):
    user_token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_user_id = models.IntegerField(blank=True, null=True, unique=True)

# Create your models here.