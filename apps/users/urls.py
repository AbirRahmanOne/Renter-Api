from django.urls import path

from knox import views as knox_views
from . views import *


urlpatterns = [
    #path('', views.index, name='name'),
    path('api/register', RegisterUserApi.as_view(),  name='register'),
    path('api/user/',  UserAPI.as_view(), name='user'),
]