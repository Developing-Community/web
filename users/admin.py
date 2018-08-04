from django.contrib import admin

# Register your models here.
from .models import Profile, ContactInfo

admin.site.register(Profile)
admin.site.register(ContactInfo)
