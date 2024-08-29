from django.db import models

# Create your models here.
class Produit (models.Model):
    designation=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=50,null=True,blank=True)
    prix=models.FloatField(default=0,null=False,blank=False)
    qt=models.FloatField(default=0,null=False,blank=False)
    image=models.ImageField(upload_to='Images/Produit', null=True, blank=True)

class Client (models.Model):
    nom_client=models.CharField(max_length=50,null=False,blank=False)
    phone=models.CharField(max_length=25,null=False,blank=False, unique=True)
    
class Facture(models.Model):
    numero=models.IntegerField(null=False,blank=False, unique=True)
    date_fact=models.DateField(auto_now_add=True)  # Enregistre la date de création
    client=models.ForeignKey(Client,on_delete=models.CASCADE)

class Transation(models.Model):
    qt_trans=models.IntegerField(default=0,blank=False)
    date_trans=models.DateField(null=False,blank=False,auto_now_add=True)  # Enregistre la date de création
    facture=models.ForeignKey(Facture,on_delete=models.CASCADE)
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    prix_unitaire=models.FloatField(default=0,blank=False)
