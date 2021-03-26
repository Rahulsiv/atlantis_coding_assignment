from django.urls import path
from .views import get_b_elements


urlpatterns = [
    path('getElement/', get_b_elements, name='get_b_elements'),
]
