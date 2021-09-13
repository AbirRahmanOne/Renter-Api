from django.urls import path

# from knox import views as knox_views
from . views import *
from . import views

urlpatterns = [
    #path('', views.index, name='name'),
    path('api/register', RegisterUserApi.as_view(),  name='register'),
    path('api/admin', UserAPI.as_view(), name='admin'),
    path('api/admins', UserList.as_view(), name='admin-list')

]