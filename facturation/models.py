from django.db import models
# Create your models here.
class Produit(models.Model):
    designation=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=50,null=False,blank=False)
    pu=models.FloatField(default=0,blank=False)
    qt=models.FloatField(null=False,default=0)
    image=models.ImageField(upload_to='Images/Produit',null=True,blank=True)

class Client(models.Model):
    nom_client=models.CharField(max_length=50,null=False,blank=False)
    phone=models.CharField( max_length=25,null=True,blank=True,unique=True)
    
class Facture(models.Model):
    numero = models.IntegerField(default=False, blank=False,unique=True)
    date_fact = models.DateField(auto_now_add=True)  # Enregistre la date de création
    client = models.ForeignKey(Client, default=0,null=False,on_delete=models.CASCADE)

class Transation(models.Model):
    qt_trans = models.IntegerField(default=0, blank=False)
    date_trans = models.DateField(null=False, blank=False)  # Enregistre la date de création
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,default=0,null=False, on_delete=models.CASCADE)
    prix_unitaire = models.FloatField(default=0, blank=False)