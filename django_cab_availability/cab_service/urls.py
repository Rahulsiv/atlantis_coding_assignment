from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/driver/register', views.register_driver, name='register_driver'),
    path('v1/<int:driver_id>/updateLocation', views.update_location, name='update_location'),
    path('v1/passenger/searchCabs', views.get_nearest_drivers, name='get_nearest_drivers'),

]
