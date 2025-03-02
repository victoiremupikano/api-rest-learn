import django
import django.db
import django.db.models
from authentication.serializer import (
    CustomTokenVerifySerializer,
    UserLoginSerializer,
    UserChangePasswordSerializer,
    UserSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User=get_user_model()


# Create your views here.
def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    return{
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

def get_data_for_user(user):
    user=User.objects.get(id=user.id)
    user=UserSerializer(user, many=False)
    return{
        'user_auth': user.data
    }

class CustomTokenVerifyView(TokenVerifyView):
    serializer_class=CustomTokenVerifySerializer

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.data.get('email')
        password=serializer.data.get('password')
        user=authenticate(email=email, password=password)
        if user is not None and user.is_active:
            token=get_tokens_for_user(user)
            data=get_data_for_user(user)
            return Response({'token': token, 'data': data, 'message': 'Connexion avec succès'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors': 'Utilisateur non reconnue'}}, status=status.HTTP_404_NOT_FOUND)
        
class UserChangePasswordView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer=UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Mot de passe changer avec succès"})
    
class UserDetailView(generics.RetrieveAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset=User.objects.all()
    serializer_class=UserSerializer

    lookup_field='pk'

class UserDeleteView(generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset=User.objects.all()
    serializer_class=UserSerializer

    lookup_field='pk'

    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        try:
            self.perform_destroy(instance)
        except django.db.models.deletion.ProtectedError as e:
            return Response(status=status.HTTP_423_LOCKED, data={'detail':str(e)})
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        return instance.delete()


