from rest_framework import serializers
from .models import Facture, Produit, Client, Transation


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produit
        fields=['id', 'designation', 'description', 'prix', 'qt']
        
    def create(self, validated_data):
        return Produit.objects.create(**validated_data)    
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client    
        fields=['nom_client', 'phone']    

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facture    
        fields=['numero', 'date_fact', 'client']         
        
class TransationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transation    
        fields=['numero', 'date_fact', 'client']           