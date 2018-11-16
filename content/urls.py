from django.urls import path

from content.models import ContentType
from .views import ContentSlugRetrieveView,ContentListView, ContentCreateView, ContentUpdateView, ContentDelete, ContentRetrieveView

app_name = 'content'
urlpatterns = [
    path('<int:pk>/', ContentRetrieveView.as_view()),
    path('get-by-slug/<str:type>/<slug:slug>/', ContentSlugRetrieveView.as_view(), name="detail-byslug"),
    path('<int:pk>/update', ContentUpdateView),
    path('list/', ContentListView.as_view()),
    path('create/', ContentCreateView.as_view()),
    path('<int:pk>/delete/', ContentDelete),
]
