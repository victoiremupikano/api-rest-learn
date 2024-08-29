from django.shortcuts import render
import django
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from services.image import add_photo
from . serializer import ClientSerializer, FactureSerializer, ProduitSerializer
from . models import Produit, Client, Facture, Transation


# Create your views here.

# produit
class ProduitDetailView(generics.RetrieveAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer
    
class ProduitListCreateView(generics.ListCreateAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer  
    
    def perform_create(self, serializer):
        image64=serializer.validated_data.get('image64')
        if image64 is None or image64 == "":
            image = None
        else:
            image=add_photo(image64)    
        serializer.save(image=image)

class ProduitUpdateView(generics.UpdateAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer   
    
    lookup_field='pk'
      
    def perform_update(self, serializer):
        image64=serializer.validated_data.get('image64')
        if image64 is None or image64 == "":
            image = None
        else:
            image=add_photo(image64)    
        serializer.save(image=image)

class ProduitDeleteView(generics.DestroyAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer   
    
    lookup_field='pk'      


# client
class ClientDetailView(generics.RetrieveAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    
class ClientListCreateView(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer  


    
class ClientUpdateView(generics.UpdateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer   
    
    lookup_field='pk'
      
class ClientDeleteView(generics.DestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer   
    
    lookup_field='pk'


# facture
class FactureDetailView(generics.RetrieveAPIView):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer
    
class FactureListCreateView(generics.ListCreateAPIView):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer  
    
    def perform_create(self, serializer):
        client_id=serializer.validated_data.get('client_id')
        client=Client.objects.get(id=client_id)
        serializer.save(client=client)
    
class FactureUpdateView(generics.UpdateAPIView):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer   
    
    lookup_field='pk'

    def perform_update(self, serializer):
        client_id=serializer.validated_data.get('client_id')
        client=Client.objects.get(id=client_id)
        serializer.save(client=client)
      
class FactureDeleteView(generics.DestroyAPIView):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer   
    
    lookup_field='pk'    