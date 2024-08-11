from django.shortcuts import render
import django
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from . serializer import ProduitSerializer
from . models import Produit, Client, Facture, Transation


# Create your views here.
class ProduitDetailView(generics.RetrieveAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer
    
class ProduitListCreateView(generics.ListCreateAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer  
    
class ProduitUpdateView(generics.UpdateAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer   
    
    lookup_field='pk'
      
class ProduitDeleteView(generics.DestroyAPIView):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer   
    
    lookup_field='pk'      