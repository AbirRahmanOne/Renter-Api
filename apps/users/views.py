from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from django.views.decorators.debug import sensitive_post_parameters
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the uers index. Abir Rahman!")


# Register User
class RegisterUserApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
        })


# # Login User API
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`

        if self.request.user.user_type == 'admin':
            queryset = self.get_queryset()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            serializer = UserSerializer(self.request.user)
            return Response(serializer.data)




        # @api_view(['GET'])ss
# def user_list(request):
#     try:
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True).data
#         return Response(serializer, status=status.HTTP_200_OK)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
