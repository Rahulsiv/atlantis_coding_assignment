from django.http import HttpResponse
from .models import ElementB, ElementBSerializer


def get_b_elements(requests):
    elements = ElementB.objects.all().order_by('id')
    serializer = ElementBSerializer(elements, many=True)
    return HttpResponse(serializer.data)
