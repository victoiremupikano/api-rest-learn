from rest_framework import serializers
from .models import Facture, Produit, Client, Transation


class ProduitSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(read_only=True)
    image64=serializers.CharField(write_only=True, allow_null=True)

    class Meta:
        model=Produit
        fields=['id', 'designation', 'description', 'prix', 'qt', 'image', 'image64']
        
    def create(self, validated_data):
        validated_data.pop('image64')
        return Produit.objects.create(**validated_data)    
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client    
        fields=['id', 'nom_client', 'phone']    

class FactureSerializer(serializers.ModelSerializer):
    client=serializers.SerializerMethodField(read_only=True)
    client_id=serializers.CharField(write_only=True, allow_null=False)

    class Meta:
        model=Facture    
        fields=['id', 'numero', 'date_fact', 'client', 'client_id']         
        
    def get_client(self, obj):
        serializer=ClientSerializer(obj.client, many=False)
        return serializer.data

class TransationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transation    
        fields=['numero', 'date_fact', 'client']           