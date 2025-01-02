from rest_framework import serializers
from rest_framework_simplejwt.serializers import (TokenVerifySerializer)
from django.contrib.auth import get_user_model
User=get_user_model()

class CustomTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        data=super(CustomTokenVerifySerializer, self).validate(attrs)
        data.update({'detail': 'Verification reussi du jeton'})
        return data

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    name=serializers.CharField(max_length=255)
    is_active=serializers.BooleanField()
    staff=serializers.BooleanField()
    password=serializers.CharField(write_only=True, allow_null=False)
    password2=serializers.CharField(write_only=True, style={'input_type':'password'})

    class Meta:
        model=User
        fields=[
            'pk', 'email', 'name', 'is_active', 'staff', 'password', 'password2'
        ]

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Mot de passe et celui de confirmation ne correspondent pas !')
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('user', None)
        email=validated_data.pop('email')
        name=validated_data.pop('name')
        staff=validated_data.pop('staff')
        is_active=validated_data.pop('is_active')
        email=validated_data.pop('email')
        password=validated_data.pop('password')

        # creation de l'utilisateur
        user=User.objects.create_user(
            email=email,
            name=name,
            staff=staff,
            is_active=is_active,
            password=password
        )
        return user

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        email=validated_data.pop('email', instance.email)
        name=validated_data.pop('name', instance.name)
        staff=validated_data.pop('staff', instance.staff)
        is_active=validated_data.pop('email', instance.is_active)

        # mise en jour
        instance.email=email
        instance.name=name
        instance.staff=staff
        instance.is_active=is_active

        instance.save()
        return instance
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email', 'password']    

class UserChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
