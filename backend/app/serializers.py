from rest_framework import serializers
from .models import *
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'user_type', 'password']
        
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        user_type = attrs.get('usertype', '')
        
        if not email:
            raise serializers.ValidationError('Users should have an Email.')
    
    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)
    
    
    
class LoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=255, min_length=3 )
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    username =serializers.CharField(max_length=255, min_length=3, read_only=True)
    user_type =serializers.CharField(max_length=255, min_length=3, read_only=True)
    
    class Meta:
        model=User
        fields = ['email',  'password', 'username', 'user_type']
    
    def validate(self, attrs):
        email =attrs.get('email', '')
        password= attrs.get('password', '')
        
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credetinals')
        
        if not user.is_active:
                raise AuthenticationFailed('Account disabled contact Admin.')
                
                
        return {
            
            'email': user.email,
            'username': user.username,
            'user_type': user.user_type
        }