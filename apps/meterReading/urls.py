from django.urls import path

from .views import *

app_name = 'meterReading'

urlpatterns = [

    path('meter-reading', RenterListAPIView.as_view(), name='meter_list'),
    path('meter-reading/<int:pk>', RenterRetrieveUpdateAPIView.as_view(), name='meter_reading_info'),
    path('meter-reading/create', RenterCreateAPIView.as_view(), name='meter_reading_create'),
    path('meter-reading/delete/<int:pk>', RenterDeleteAPIView.as_view(), name='meter_reading_delete'),
]
