import os, errno

from fogsys.settings import CLOUD_DIR

from django.db import models

from .utils import create_hash


class SensorType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.name

    def save(self, commit=True):
        try:
            os.mkdir(os.path.join(CLOUD_DIR, self.name))
            
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        super(SensorType, self).save()

    class Meta:
        verbose_name = 'Tipo'


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    secure_hash = models.CharField(max_length=64, editable=False)
    location = models.CharField(max_length=255, verbose_name='Localização')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    sensor_type = models.ForeignKey(SensorType, null=True, on_delete=models.SET_NULL, verbose_name='Tipo')

    def save(self, *args, **kwargs):
        self.secure_hash = create_hash(self.name)
        super(Sensor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'