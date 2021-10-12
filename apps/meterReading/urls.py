from django.urls import path

from .views import *

app_name = 'meterReading'

urlpatterns = [

    path('', MeterReadingListAPIView.as_view(), name='meter_reading_list'),
    path('<int:pk>', MeterReadingRetrieveUpdateAPIView.as_view(), name='meter_reading_info'),
    path('create', MeterReadingCreateAPIView.as_view(), name='meter_reading_create'),
    path('delete/<int:pk>', MeterReadingDeleteAPIView.as_view(), name='meter_reading_delete'),
]
