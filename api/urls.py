from django.urls import path
from . import views

from .views import FlatListView, FlatRetrieveView, FlatCreateView, FlatRetrieveUpdateView, FlatDeleteView

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', FlatListView.as_view(), name='flat_list'),
    path('api/<int:pk>', FlatRetrieveUpdateView.as_view(), name='flat_info'),
    path('api/create', FlatCreateView.as_view(), name='create_flat'),
    path('api/delete/<int:pk>', FlatDeleteView.as_view(), name='delete_flat'),
]

