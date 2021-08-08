from rest_framework import generics, permissions
from rest_framework import serializers
from .models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type']


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}} #Q

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_type = validated_data.pop('user_type')
        user = User.objects.create_user(
            **validated_data
            # username= validated_data['username']

        )
        user.set_password(password)
        user.user_type = user_type
        user.save()
        return user

