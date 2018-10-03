from django.db import models

import uuid

class TelegramToken(models.Model):
    verify_token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_user_id = models.IntegerField()

# Create your models here.
