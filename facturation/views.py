# importation du django et django restframework
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import  generics
from facturation.services.images import add_photo
# importation des modesls
from facturation.models import Produit, Client, Facture, Transation 
# importation des serializers
from .serializer import ProduitSerializer,ClientSerializer,FactureSerializer,TransactionSerializer
# Create your views here.
# views produits
class ProduitDetailView(generics.RetrieveAPIView):
    queryset = Produit.objects.all()  # pylint: disable=E1101
    serializer_class = ProduitSerializer
    
class ProduitListCreate(generics.ListCreateAPIView):
    queryset=Produit.objects.all()  # pylint: disable=E1101
    serializer_class=ProduitSerializer
    
    def perform_create(self,serializer):
        image64=serializer.validated_data.get('image64')
        if image64 is None or image64 =="":
            image=None
        else:
            image=add_photo(image64)
        serializer.save(image=image)
    
class ProduitUpdateView(generics.UpdateAPIView):
    queryset=Produit.objects.all()    # pylint: disable=E1101
    serializer_class=ProduitSerializer
    lookup_field='pk'
    
    def perform_update(self,serializer):
        image64=serializer.validated_data.get('image64')
        if image64 is None or image64 =="":
             image=None
        else:
            image=add_photo(image64)
        serializer.save(image=image)
    
    
class ProduitDeleteView(generics.DestroyAPIView):
    queryset=Produit.objects.all()      # pylint: disable=E1101
    serializer_class=ProduitSerializer
    lookup_field='pk'


# View for Customers 
class ClientDetailView(generics.RetrieveAPIView):
    # voir une selection de tous les tuplet de la table 
    queryset=Client.objects.all()  # pylint: disable=E1101
    serializer_class=ClientSerializer

class ClientListCreate(generics.ListCreateAPIView):
    queryset=Client.objects.all()  # pylint: disable=E1101
    serializer_class=ClientSerializer

class ClientUpdateView(generics.UpdateAPIView):
    queryset=Client.objects.all()  # pylint: disable=E1101
    serializer_class=ClientSerializer
    lookup_field='pk'
    
class ClientDeleteView(generics.DestroyAPIView):
    queryset=Client.objects.all()  # pylint: disable=E1101
    serializer_class=ClientSerializer
    lookup_field='pk'
    
# views for facture.
class FactureDetailView(generics.RetrieveAPIView):
    queryset = Facture.objects.all()  # pylint: disable=E1101
    serializer_class = FactureSerializer
    
class FactureListCreate(generics.ListCreateAPIView):
    queryset=Facture.objects.all()  # pylint: disable=E1101
    serializer_class=FactureSerializer
    
    def perform_create(self,serializer):
        client_id=serializer.validated_data.get('client_id')
        client=Client.objects.get(id=client_id)
        serializer.save(client=client)

class FactureUpdateView(generics.UpdateAPIView):
    queryset=Facture.objects.all()    # pylint: disable=E1101
    serializer_class=FactureSerializer
    lookup_field='pk'
    
    def perform_update(self,serializer):
        client_id=serializer.validated_data.get('client_id')
        client=Client.objects.get(id=client_id)
        serializer.save(client=client)
    
class FactureDeleteView(generics.DestroyAPIView):
    queryset=Facture.objects.all()      # pylint: disable=E1101
    serializer_class=FactureSerializer
    lookup_field='pk'

# views transaction
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
        serializer.save(facture=facture)
        
        produit_id=serializer.validated_data.get('produit_id')
        produit=Produit.objects.get(id=produit_id)
        serializer.save(produit=produit)
    
    
 # UpdateAPIView est une methode generic qui permet la modification  des donnees
class TransactionUpdateView(generics.UpdateAPIView):
    queryset=Transation.objects.all()    # pylint: disable=E1101
    serializer_class=TransactionSerializer
    lookup_field='pk'
    
    def perform_update(self,serializer):
        facture_id=serializer.validated_data.get('facture_id')
        facture=Facture.objects.get(id=facture_id)
        serializer.save(facture=facture)
        
        produit_id=serializer.validated_data.get('produit_id')
        produit=Produit.objects.get(id=produit_id)
        serializer.save(produit=produit)
    
  # DestroyAPIView est une methode generic qui permet la suppression des donnees  
class TransactionDeleteView(generics.DestroyAPIView):
    queryset=Transation.objects.all()      # pylint: disable=E1101
    serializer_class=TransactionSerializer
    lookup_field='pk'
    
    