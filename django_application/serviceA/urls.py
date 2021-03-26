from django.urls import path
from .views import get_a_elements, add_a_elements, update_a_elements


urlpatterns = [
    path('getElement/', get_a_elements, name='get_a_elements'),
    path('addElement/', add_a_elements, name='add_a_elements'),
    path('<int:element_id>/updateElement/', update_a_elements, name='update_a_elements'),
]
