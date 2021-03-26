from rest_framework import serializers
from django.db import models


class ElementB(models.Model):
    element_id = models.IntegerField(unique=True, blank=True, null=True)
    sample_name = models.CharField(max_length=100)
    sample_number = models.IntegerField(default=0)


class ElementBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementB
        fields = '__all__'


def handle_new_element_a(sender, instance, created, **kwargs):
    element = ElementB.objects.filter(element_id=instance.id).first()
    if not element:
        element = ElementB.objects.create(sample_name=instance.sample_name, sample_number=instance.sample_number,
                                          element_id=instance.id)
        serializer_data = ElementBSerializer(element).data
        print('element added in B')
    else:
        element.sample_name = instance.sample_name
        element.sample_number = instance.sample_number
        element.save()
        print('element updated in B')


def handle_deleted_element_a(sender, instance, **kwargs):
    element = instance
    element_b = ElementB.objects.filter(sample_name=element.sample_name, sample_number=element.sample_number).first()
    if element_b:
        element_b.delete()
    print('element removed from B')
