from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


# Create your views here.

class FlatListAPIView(ListAPIView):
 #   permission_classes = [IsAuthenticated]
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

#
class FlatCreateAPIView(CreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDeleteAPIView(DestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
