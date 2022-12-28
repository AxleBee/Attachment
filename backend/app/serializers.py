from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'user_type', 'password']
        
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        user_type = attrs.get('user_type', '')
        
        if not email:
            raise serializers.ValidationError('Users should have an Email.')
        
        return attrs
    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)
    
    
    
class LoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=255, min_length=3 )
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    username =serializers.CharField(max_length=255, min_length=3, read_only=True)
    user_type =serializers.CharField(max_length=255, min_length=3, read_only=True)
    authenticated = serializers.BooleanField(read_only=True)
    class Meta:
        model=User
        fields = ['email',  'password', 'username', 'user_type', 'authenticated']
    
    def validate(self, attrs):
        email =attrs.get('email', '')
        password= attrs.get('password', '')
        
        
        user = authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credetinals')
        
        if not user.is_active:
                raise AuthenticationFailed('Account disabled contact Admin.')
                
        return {
            
            'email': user.email,
            'username': user.username,
            'user_type': user.user_type, 
            'authenticated': user
        }
        
        
        
class StudentSerializer(serializers.ModelSerializer):
    
    admission_no = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=255)
    course = serializers.CharField(max_length=255)
    department = serializers.CharField(max_length=255)
    photo_url = serializers.ImageField(required=False)
    user = serializers.ReadOnlyField(source='user.email')
    
    
    class Meta:
        model = Student
        fields = ['admission_no', 'name', 'course', 'department', 'photo_url', 'user']

    def validate(self, attrs):
        admission =attrs.get('admission_no', '')
        
        if not admission:
            raise ValueError("Student must have admission number")
        
        return attrs
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        
        
        
        
        
        
    
      