from django.db import models
from rest_framework import exceptions
from rest_framework import serializers


class Driver(models.Model):
    name = models.CharField(max_length=255)
    car_number = models.CharField(unique=True, max_length=25, db_index=True)
    phone_number = models.CharField(unique=True, max_length=15, db_index=True)
    license_number = models.CharField(unique=True, max_length=25, db_index=True)
    email = models.EmailField(unique=True, max_length=255, db_index=True)
    latitude = models.FloatField(blank=True, null=True, db_index=True)
    longitude = models.FloatField(blank=True, null=True, db_index=True)

    def __str__(self):
        return self.name


class DriverDoestNotExist(exceptions.APIException):
    status_code = 400
    default_code = 'Driver does not exist'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
