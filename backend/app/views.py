from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate ,login, logout
from rest_framework.decorators import api_view
from .models import *
# Create your views here.


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


# class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.data['email']).first()
        if (serializer.data['authenticated']):
            print(request.user)
            # login(request, user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def login_user(request):
    
    attrs = request.data
    user = authenticate(request, email = attrs.get('email'), password = attrs.get('password'))
    if user is not None:
        login(request, user)
    else:
        raise AuthenticationFailed('Invalid credetinals')
    print(request.user.is_authenticated)
    user_data = {
            'email': user.email,
            'username': user.username,
            'user_type': user.user_type,
            'authenticated':request.user.is_authenticated 
    }
    
    return Response(user_data, status=status.HTTP_200_OK)

@api_view(["GET"])
def logout_user(request):
    logout(request)

    return Response('User Logged out successfully')

class StudentAPIView(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def user_logout(request):
    pass
