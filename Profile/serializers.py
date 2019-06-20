#-------------LIBRERIAS----------

from rest_framework import routers, serializers, viewsets

# from drf_dynamic_fields import DynamicFieldsMixin

#----------------Modelos---------
#     nombre App           nombre modelo
from  Profile.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= ('id','name','ap_pat','ap_mat','year','img')