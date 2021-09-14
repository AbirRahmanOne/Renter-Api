from django.urls import path

# from knox import views as knox_views
from . views import *
from . import views

urlpatterns = [
    #path('', views.index, name='name'),
    path('register', RegisterUserApi.as_view(),  name='register'),
    path('admin', UserAPI.as_view(), name='admin'),
    path('admins', UserList.as_view(), name='admin-list')

]