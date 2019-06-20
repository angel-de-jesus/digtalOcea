

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
from Cliente.models import Cliente

# ----------------serializers-------------
from Cliente.serializers import ClienteSerializers

# ------------------LIBRERIAS EXTERNAS------------------
# import json

class ClienteList(APIView):
    #METODO PARA EXPLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Cliente.objects.filter(delete = False)
        serializer = ClienteSerializers(queryset, many=True)
        return Response(serializer.data)
    # METODO PARA CREAR NUEVO REGISTRO 
    def post(self, request, format=None):
        serializer = ClienteSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas, status=status.HTTP_201_CREATED)
    

    
    # def put(self, request,pk ,format=None):
    #     cliente= Cliente.objects.get(pk=pk)
    #     serializer = ClienteSerializers(cliente, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):

    # METODO PARA CONSULTAR EL ID Y ME RETORNE SI EXISTE
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return "No"
    
    # METODO PARA CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request,pk ,format=None):
        Id = self.get_object(pk)
        if Id !="No":
            Id=ClienteSerializers(Id)
            return Response(Id.data)
        return Response("No Existe")

    # METODO PARA CONSULTAR EL ID Y ACTUALIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request,pk ,format=None):
        Id = self.get_object(pk)
        serializer=ClienteSerializers(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response('Error', status=status.HTTP_400_BAD_REQUEST)
