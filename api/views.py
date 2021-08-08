from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.generics import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

import logging
from rest_framework.views import exception_handler
from django.http import JsonResponse
from requests import ConnectionError


# Create your views here.



def index(request):
    return HttpResponse('Hello, we are in RMS server!')


class FlatListView(ListAPIView):
    authentication_classes = [ SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatRetrieveView(RetrieveAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatCreateView(CreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDeleteView(DestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


# @api_view(['GET'])
# def flat_list(request):
#     try:
#         flats = Flat.objects.all().order_by('name')
#         serializer = FlatSerializer(flats, many=True).data
#         return Response(serializer, status=status.HTTP_200_OK)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET'])
# def flat_info(request, pk):
#     try:
#         flat = Flat.objects.get(id=pk)
#         serializer = FlatSerializer(flat, many=False).data
#         return Response(serializer, status=status.HTTP_200_OK)
#     except:
#         error_msg = {"Message": "No Data Found"}
#         return JsonResponse(error_msg, status=status.HTTP_400_BAD_REQUEST)
#         # return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def flat_create(request):
#     flat = FlatSerializer(data=request.data)
#
#     if flat.is_valid():
#         flat.save()
#         return Response(flat.data, status=status.HTTP_201_CREATED)
#     return Response(flat.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT', 'PATCH'])
# def flat_update(request, pk):
#     try:
#         flat = Flat.objects.get(pk=pk)
#     except:
#         message = {
#             'message': 'Data does not exist'
#         }
#         return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
#
#     serializer = FlatSerializer(instance=flat, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['DELETE'])
# def flat_delete(request, pk):
#     try:
#         flat = Flat.objects.get(pk=pk)
#         flat.delete()
#         message = {
#             'message': 'Item deleted Successfully!',
#         }
#         return JsonResponse(message, status=status.HTTP_200_OK)
#     except:
#         message = {
#             'message': 'Data does not exist'
#         }
#         return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
