#-------------LIBRERIAS----------

from rest_framework import routers, serializers, viewsets

#----------------Modelos---------
#     nombre App             nombre modelo
from  Cliente.models import Cliente

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields= ('id','name','ap_pat','ap_mat','year')