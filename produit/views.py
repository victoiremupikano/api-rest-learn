from django.shortcuts import render
import django
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from services.mixins import QSFilterWithFacture
from services.image import add_photo
from . serializer import ClientSerializer, FactureSerializer, ProduitSerializer, TransactionSerializer
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

# transaction
class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transation.objects.all()  # pylint: disable=E1101
    serializer_class = TransactionSerializer
    
    # ListCreateAPIView est une methode generic qui permet de lister plusieurs itemes et de creer les donnees

class TransactionListCreate(generics.ListCreateAPIView):
    queryset=Transation.objects.all()  # pylint: disable=E1101
    serializer_class=TransactionSerializer
    
    def perform_create(self,serializer):
        facture_id=serializer.validated_data.get('facture_id')
        facture=Facture.objects.get(id=facture_id)        
        produit_id=serializer.validated_data.get('produit_id')
        produit=Produit.objects.get(id=produit_id)
        serializer.save(facture=facture, produit=produit)

class TransactionWithFactureListCreate(
    QSFilterWithFacture,
    generics.ListAPIView):
    queryset=Transation.objects.all()  # pylint: disable=E1101
    serializer_class=TransactionSerializer    
    
class TransactionUpdateView(generics.UpdateAPIView):
    queryset=Transation.objects.all()    # pylint: disable=E1101
    serializer_class=TransactionSerializer
    lookup_field='pk'
    
    def perform_update(self,serializer):
        facture_id=serializer.validated_data.get('facture_id')
        facture=Facture.objects.get(id=facture_id)        
        produit_id=serializer.validated_data.get('produit_id')
        produit=Produit.objects.get(id=produit_id)
        serializer.save(facture=facture, produit=produit)
    
  # DestroyAPIView est une methode generic qui permet la suppression des donnees  

class TransactionDeleteView(generics.DestroyAPIView):
    queryset=Transation.objects.all()      # pylint: disable=E1101
    serializer_class=TransactionSerializer
    lookup_field='pk'
    
     