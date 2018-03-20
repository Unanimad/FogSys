from django.contrib import admin

from .models import *

class SensorTypeAdmin(admin.ModelAdmin):
    pass

class SensorAdmin(admin.ModelAdmin):
    pass

admin.site.register(SensorType, SensorTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
