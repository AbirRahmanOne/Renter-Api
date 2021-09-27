from django.urls import path

from .views import *


urlpatterns = [

    path('renters', RenterListAPIView.as_view(), name='renter_list'),
    path('renter/<int:pk>', RenterRetrieveUpdateAPIView.as_view(), name='renter_info'),
    path('renter/create', RenterCreateAPIView.as_view(), name='renter_create'),
    path('renter/delete/<int:pk>', RenterDeleteAPIView.as_view(), name='renter_delete'),
]
