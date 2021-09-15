from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from apps.users.permissions import IsAdmin, IsModerator
from .models import *


# Create your views here.

class FlatListAPIView(ListAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    permission_classes = [IsAuthenticated | IsAdmin | IsModerator]


class FlatCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
