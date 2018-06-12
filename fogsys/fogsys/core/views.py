import datetime
import random
import decimal

from django.http import JsonResponse

from fogsys.settings import CLOUD_DIR

from .models import *


def save_measurement(self, sensor_pk, measurement, hash):
    try:
        sensor = Sensor.objects.get(pk=int(sensor_pk), secure_hash=hash)
        now = datetime.datetime.now()

        sensor_dir = os.path.join(
            CLOUD_DIR, 'production_measurement', sensor.sensor_type.name)
        year_dir = os.path.join(sensor_dir, str(now.year))
        month_dir = os.path.join(sensor_dir, str(now.year), str(now.month))
        day_dir = os.path.join(sensor_dir, str(now.year),
                            str(now.month), str(now.day))
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
            'error': False,
            'sensor': sensor.name,
            'sensor_type': sensor.sensor_type.name,
            'measurement': float(measurement),
            'error': 0,
        }

    except Sensor.DoesNotExist:
        context = {
            'error': True,
            'text': 'Sensor não encontrado'
        }

    return JsonResponse(context)


def test_measurement(self):
    context = []
    sensors = Sensor.objects.all()

    for sensor in sensors:
        measurements = []
        # generate a random int number to count measurements
        count_measurement = random.randint(0, 100)

        for count in range(count_measurement):
            # generate a random decimal number between 1 and 100
            measurement = str(decimal.Decimal(random.randrange(1, 1000))/10)
            now = datetime.datetime.now()

            sensor_dir = os.path.join(
                CLOUD_DIR, 'test_measurement', sensor.sensor_type.name)

            year_dir = os.path.join(sensor_dir, str(now.year))
            month_dir = os.path.join(sensor_dir, str(now.year), str(now.month))
            day_dir = os.path.join(sensor_dir, str(
                now.year), str(now.month), str(now.day))

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

            measurements.append({
                'time': str(now.hour) + ':' + str(now.minute),
                'measurement': measurement
            })

        context.append({
            'sensor': sensor.name,
            'measurements': measurements
        })

        print(context)

    return JsonResponse(context, safe=False)
