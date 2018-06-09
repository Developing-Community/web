from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register_view, name='register'),
]