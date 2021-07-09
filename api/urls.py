from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/flat-list/', views.flat_list, name='flat-list'),
    path('api/flat-info/<str:pk>', views.flat_info, name='flat-info'),
    path('api/create-flat', views.flat_create, name='create-flat'),
    path('api/update-flat/<str:pk>', views.flat_update, name='update-flat'),
    path('api/delete-flat/<str:pk>', views.flat_delete, name='delete-flat'),
]

