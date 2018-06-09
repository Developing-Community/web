from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

app_name = 'siteinfo'
urlpatterns = [
    # ex: /polls/
    path('', views.index_view, name='index'),
    path('groups/', views.groups_view, name='groups'),
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/img/favicon.ico',  permanent=True), name='icon'),
    re_path(r'^robots\.txt$',RedirectView.as_view(url='/static/robots.txt',  permanent=True), name='robots.txt'),
    path('trello/link', RedirectView.as_view(url='https://trello.com/invite/developingcommunity/0569c91ef09c6c05f437a75927640874', permanent=True), name='trello'),
    path('slack/link', RedirectView.as_view(url='https://join.slack.com/t/developing-community/shared_invite/enQtMzc1ODU0NTA5MzAzLTE0NmI1MmY4ZGM5NjhiODY2MDFjNmFjYjg1OWExNTBjZmViMjRkMWE4Y2U1NDk1ZjdjYzM5ODhlZmYwZWQ0MTA', permanent=True), name='slack'),
    # # ex: /polls/5/
    # # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]