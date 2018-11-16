from django.contrib import admin

from .models import Content, ContentRelation

admin.site.register(Content)
admin.site.register(ContentRelation)
