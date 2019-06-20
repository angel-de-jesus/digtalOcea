# ------------Librerias------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Esp32.models import Esp32
# ----------------serializers-------------
from Esp32.serializers import Esp32Serializers

# ------------------LIBRERIAS EXTERNAS------------------
# import json

class Esp32List(APIView):
    # METODO PARA EXPLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Esp32.objects.filter(delete=False)
        #                               ,context = {'request':request}
        serializer = Esp32Serializers(queryset, many=True, context = {'request':request})
        return Response(serializer.data)
    # METODO PARA CREAR NUEVO REGISTRO 
    def post(self, request, format=None):
        serializer = Esp32Serializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Esp32Detail(APIView):
    #METODO PARA COSULTAR ID Y E RETORNE SI EXISTE O NO
    def get_object(self,pk):
        try: 
            return Esp32.objects.get(pk=pk)
        except Esp32.DoesNotExist:
            raise Http404
    #METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS 
    def get(self, request,pk, format=None):
        Esp32 = self.get_object(pk) 
        serializer = Esp32Serializers(Esp32)
        return Response(serializer.data)
    #METODO CONSULTAR ID Y ACTUALIZAR DATOS 
    def put(self, request,pk, format=None):
        Esp32 = self.get_object(pk)
        serializer = Esp32Serializers(Esp32, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Esp32 = self.get_object(pk)
        serializer = Esp32Serializers(Esp32, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)