from django.urls import path, re_path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
