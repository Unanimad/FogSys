# Generated by Django 2.0.3 on 2018-03-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Localização'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
    ]
