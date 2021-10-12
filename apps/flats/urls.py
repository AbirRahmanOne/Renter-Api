from django.urls import path
from django.urls import path
from . import views

from .views import FlatListAPIView, FlatRetrieveUpdateAPIView, FlatDeleteAPIView, FlatCreateAPIView

app_name = 'flats'

urlpatterns = [

    path('flats', FlatListAPIView.as_view(), name='flat_list'),
    path('flat/<int:pk>', FlatRetrieveUpdateAPIView.as_view(), name='flat_info'),
    path('flat/create', FlatCreateAPIView.as_view(), name='flat_create'),
    path('flat/delete/<int:pk>', FlatDeleteAPIView.as_view(), name='flat_delete'),
]

