from django.urls import path

from .views import *

app_name = 'fogsys'
ulspatterns = [
    path('<int:sensor_pk>/<int:type_pk>/(?P<measurement>\w+)', save_measurement, name='measurement')
]