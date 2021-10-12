from django.shortcuts import render

import django_filters.rest_framework
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from apps.users.permissions import IsAdmin, IsModerator

from .models import *


class RenterListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated | IsAdmin | IsModerator]
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer

    #filter
    

    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # django_filters = ['flat']

    # def get_queryset(self, value):
    #     return MeterReading.objects.filter(flat=value)





class RenterCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer


class RenterRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer


# This is testing purpose will be deleted in future
class RenterDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = MeterReading.objects.all()
    serializer_class = MeterReadingSerializer
