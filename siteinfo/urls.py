from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index_view, name='index'),
    path('art/', views.art_view, name='art'),
    # # ex: /polls/5/
    # # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]