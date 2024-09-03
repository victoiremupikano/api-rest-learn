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
    
    def create(self, validated_data):
        validated_data.pop('client_id')
        return Facture.objects.create(**validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    facture=serializers.SerializerMethodField(read_only=True)
    facture_id=serializers.CharField(write_only=True,allow_null=False)
    produit=serializers.SerializerMethodField(read_only=True)
    produit_id=serializers.CharField(write_only=True,allow_null=False)
    
    class Meta:
        model = Transation
        fields = ['id', 'qt_trans', 'date_trans', 'facture', 'facture_id', 'produit', 'produit_id', 'prix_unitaire']
    
    def get_produit(self,obj):
        serializer=ProduitSerializer(obj.produit,many=False)
        return serializer.data
    
    def get_facture(self,obj):
        serializer=FactureSerializer(obj.facture,many=False)
        return serializer.data
    
    def create(self,validated_data):
        validated_data.pop('facture','produit')
        return Transation.objects.create(**validated_data)