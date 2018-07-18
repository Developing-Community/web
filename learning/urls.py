from django.urls import path

from .views import (
    add_mentoring,
)

app_name = 'mentoring'
urlpatterns = [
    path('add/', add_mentoring, name='add_mentoring'),
]