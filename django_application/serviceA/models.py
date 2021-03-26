from django.db import models
from rest_framework import serializers
from serviceB.models import handle_deleted_element_a, handle_new_element_a


class ElementA(models.Model):
    sample_name = models.CharField(max_length=100)
    sample_number = models.IntegerField(default=0)


class ElementASerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementA
        fields = '__all__'


models.signals.post_save.connect(receiver=handle_new_element_a, sender=ElementA)
models.signals.pre_delete.connect(receiver=handle_deleted_element_a, sender=ElementA)