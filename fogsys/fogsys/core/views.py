import datetime

from django.http import JsonResponse

from fogsys.settings import CLOUD_DIR

from .models import *


def save_measurement(self, sensor_pk, type_pk, measurement):
    sensor = Sensor.objects.get(pk=int(sensor_pk))
    sensor_type = SensorType.objects.get(pk=int(type_pk))

    now = datetime.datetime.now()

    sensor_dir = os.path.join(CLOUD_DIR, sensor_type.name)
    year_dir = os.path.join(sensor_dir, str(now.year))
    month_dir = os.path.join(sensor_dir, str(now.year), str(now.month))
    day_dir = os.path.join(sensor_dir, str(now.year), str(now.month), str(now.day))
    file_dir = day_dir

    if not os.path.exists(sensor_dir):
        os.mkdir(sensor_dir)

    if not os.path.exists(year_dir):
        os.mkdir(year_dir)

    if not os.path.exists(month_dir):
        os.mkdir(month_dir)

    if not os.path.exists(day_dir):
        os.mkdir(day_dir)

    f = open(file_dir + '/' + sensor.name + '.txt', 'a')
    f.write(str(now.hour) + ':' + str(now.minute) + ' ' + measurement + '\n')
    f.close()
        
    context = {
        'sensor': sensor.name,
        'sensor_type': sensor_type.name,
        'measurement': float(measurement),
        'error': 0,
    }

    return JsonResponse(context)