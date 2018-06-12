from django.contrib import admin

from .models import *

class SensorTypeAdmin(admin.ModelAdmin):
    pass

class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'secure_hash', 'location', 'sensor_type', 'created_at')
    list_filter = ['sensor_type', 'created_at']
    search_fields = ['name', 'location']

admin.site.register(SensorType, SensorTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
