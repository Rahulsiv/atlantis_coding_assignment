from django.http import HttpResponse
from .models import Driver, DriverDoestNotExist, DriverSerializer
from .services import DistanceClass
import json


def register_driver(request):
    try:
        request_body = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponse({
            'error': True,
        })
    serializer = DriverSerializer(data=request_body)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse({
            'success': True
        })
    else:
        return HttpResponse(
            serializer.errors
        )


def update_location(request, driver_id):
    """
    :param request: json.dumbs ->  {"latitude" : 34.0023, "longitude": -43.0000}
    :param driver_id: driver id
    """
    try:
        request_body = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponse({
            'error': True,
        })
    try:
        driver = Driver.objects.get(id=driver_id)
    except Driver.DoesNotExist:
        raise DriverDoestNotExist
    driver_data = driver.__dict__
    driver_data['latitude'] = float(request_body.get('latitude'))
    driver_data['longitude'] = float(request_body.get('longitude'))
    serializer = DriverSerializer(driver, data=driver_data)
    if serializer.is_valid():
        driver.save()
        return HttpResponse({
            'success': True
        })
    else:
        return HttpResponse(
            serializer.errors
        )


def get_nearest_drivers(request):
    try:
        request_body = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponse({
            'error': True,
        })
    dist_class = DistanceClass()
    lat = request_body.get('latitude')
    lon = request_body.get('longitude')
    drivers = Driver.objects.exclude(
        latitude=None).exclude(longitude=None).values_list('latitude', 'longitude', 'id')
    nearby_driver_ids = list()
    for driver in drivers:
        distance = dist_class.calculate_distance(driver[0], driver[1], lat, lon)
        # ignoring all drivers who are more than 4 kms away from passenger's coordinates
        if distance <= 4:
            nearby_driver_ids.append(driver[2])
    nearby_drivers = Driver.objects.filter(id__in=nearby_driver_ids)
    serializer = DriverSerializer(nearby_drivers, many=True)
    response = serializer.data
    return HttpResponse(response)
