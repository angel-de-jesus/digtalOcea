#-------------LIBRERIAS----------

from rest_framework import routers, serializers, viewsets

#----------------Modelos---------
#     nombre App                  nombre modelo
from  Administrador.models import Administrador

class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields= ('id','name','ap_pat','ap_mat','year')