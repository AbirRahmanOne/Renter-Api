from django.shortcuts import render

from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from apps.users.permissions import IsAdmin, IsModerator

from .models import *


class RenterListAPIView(ListAPIView):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
    permission_classes = [IsAuthenticated | IsAdmin | IsModerator]


class RenterCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class RenterRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


# This is testing purpose will be deleted in future
class RenterDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated & IsAdmin]
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
