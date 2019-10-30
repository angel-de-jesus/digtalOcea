# Generated by Django 2.2.1 on 2019-06-10 19:42

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Esp32',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_esp32', models.CharField(max_length=100)),
                ('delete', models.BooleanField(default=False)),
                ('date_now', models.DateTimeField(default=django.utils.timezone.now)),
                ('mac_esp32', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Esp32',
            },
        ),
    ]