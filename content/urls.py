from django.urls import path

from .views import ContentListView, ContentCreateView, ContentUpdateView, ContentDelete, ContentRetrieveView

app_name = 'content'
urlpatterns = [
    path('<int:pk>/', ContentRetrieveView.as_view()),
    path('<int:pk>/update', ContentUpdateView),
    path('list/', ContentListView.as_view()),
    path('create/', ContentCreateView.as_view()),
    path('<int:pk>/delete/', ContentDelete),
]
