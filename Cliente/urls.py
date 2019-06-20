from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from Cliente import views


urlpatterns = [
    re_path(r'^cliente/$', views.ClienteList.as_view()),
    re_path(r'^listaCliente/(?P<pk>\d+)$', views.ClienteDetail.as_view()),
]