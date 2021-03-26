from django.urls import path

from . import views

urlpatterns = [
    path('', views.CSVFileView.as_view(), name='index'),
]
