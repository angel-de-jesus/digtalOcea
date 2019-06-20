from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from Estudiante import views


urlpatterns = [
    re_path(r'^Estudiante/$', views.EstudianteList.as_view()),
    re_path(r'^listaEstudiante/(?P<pk>\d+)$', views.EstudianteDetail.as_view()),

]