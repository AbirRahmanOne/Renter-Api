from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *
# Create your views here.


def index(request):
    return HttpResponse('Hello, we are in RMS server!')


@api_view(['GET'])
def flat_list(request):
    try:
        flats = Flat.objects.all()
        data = FlatSerializer(flats, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def flat_info(request, pk):
    try:
        flat = Flat.objects.get(id=pk)
        data = FlatSerializer(flat, many=False).data
        return Response(data, status=status.HTTP_200_OK)
    except:
        data = { "Message": "No Data Found"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
        # return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def flat_create(request):
    new_flat = FlatSerializer(data=request.data)

    if new_flat.is_valid():
        new_flat.save()
        return Response(new_flat.data, status=status.HTTP_201_CREATED)
    return Response(new_flat.errors, status=status.HTTP_400_BAD_REQUEST)





