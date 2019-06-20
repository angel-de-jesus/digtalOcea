# ----------------librerias------------
from rest_framework import routers, serializers, viewsets

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Esp32.models import Esp32

from drf_dynamic_fields import DynamicFieldsMixin
#                         serializers
class Esp32Serializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Esp32
        fields = ('id','id_user','num_esp32','mac_esp32','delete')

