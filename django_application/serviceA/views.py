from django.http import HttpResponse
from .models import ElementA, ElementASerializer
import json


def get_a_elements(requests):
    elements = ElementA.objects.all().order_by('id')
    serializer = ElementASerializer(elements, many=True)
    return HttpResponse(serializer.data)


def add_a_elements(requests):
    """
    :param requests: json.dumps of { "sample_name": "Tester123", "sample_number': 10 }
    :return: success: True
    """
    request_body = json.loads(requests.body)
    serializer = ElementASerializer(data=request_body)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse({
            'success': True
        })


def update_a_elements(requests, element_id):
    """
    :param element_id: id of element to update
    :param requests: json.dumps of { "sample_name": "Tester123", "sample_number': 10 }
    :return: success: True
    """
    try:
        ea = ElementA.objects.get(id=element_id)
    except ElementA.DoesNotExist:
        return HttpResponse({
            'status': False,
            'error': 'Bad Request'
        })
    request_body = json.loads(requests.body)
    body = ea.__dict__
    for each in body:
        if each in request_body:
            body[each] = request_body[each]
    serializer = ElementASerializer(ea, data=body)
    if serializer.is_valid():
        return HttpResponse({
            'success': True
        })
