# from django.contrib.auth.models import Profesor
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.contrib.auth.models import User
# from django.contrib.auth.models import Profesor
# from django.core.exceptions.
from django.utils import timezone

class Esp32(models.Model):
    id_user = models.ForeignKey(User, on_delete = models.SET(-1))
    num_esp32 = models.CharField(max_length=100, null=False)
    mac_esp32 = models.CharField(max_length=100, null=False)
    delete = models.BooleanField(default=False)
    date_now = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Esp32'