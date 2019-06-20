#-------------LIBRERIAS----------

from rest_framework import routers, serializers, viewsets

#----------------Modelos---------
#     nombre App           nombre modelo
from  Estudiante.models import Estudiante

class EstudianteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields= ('id','name','ap_pat','ap_mat','year')