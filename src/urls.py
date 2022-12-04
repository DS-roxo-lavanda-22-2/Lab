from django.urls import include, path

from . import views

urlpatterns = [
  path('', views.list_users, name='list_users'),
  path('create', views.create_user, name='create_user'),
]