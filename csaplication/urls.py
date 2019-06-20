
# from django.contrib import admin
# from django.urls import path
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# from django.conf import settings
# from django.conf.urls.static import static


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/login', include('login.urls')),
    re_path(r'^api/v1/admin/', include('Administrador.urls')),
    re_path(r'^api/v1/estudiante/', include('Estudiante.urls')),
    re_path(r'^api/v1/cliente/', include('Cliente.urls')),
    re_path(r'^api/v1/profile/', include('Profile.urls')),
    re_path(r'^api/v1/profesor/', include('Profesor.urls')),
    re_path(r'^api/v1/alumno/', include('Alumno.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^api/v1/Esp32/', include('Esp32.urls')),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
