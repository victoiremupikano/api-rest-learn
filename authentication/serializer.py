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
    is_active=serializers.BooleanField(read_only=True)
    staff=serializers.BooleanField(read_only=True)
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
        password=validated_data.pop('password')

        # creation de l'utilisateur
        user=User.objects.create_user(
            email=email,
            name=name,
            password=password
        )
        return user

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        email=validated_data.pop('email', instance.email)
        name=validated_data.pop('name', instance.name)

        # mise en jour
        instance.email=email
        instance.name=name

        instance.save()
        return instance
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email', 'password']    

class UserChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password2=serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)

    class Meta:
        fields=['password', 'password2']

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        # recuperation de l'utilisateur connecter
        user=self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Le mot de passe  et celle de confirmation ne correspondent pas")
        user.set_password(password)
        user.save()
        return attrs