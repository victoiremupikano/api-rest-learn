from django.conf import settings
from django.db import models
# Create your models here.
class Produit(models.Model):
    designation=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=50,null=False,blank=False)
    pu=models.FloatField(null=False,blank=False)
    qt=models.FloatField(null=False,blank=False)
    image=models.ImageField(upload_to='Images/Produit',null=True,blank=True)
    User=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False,
        default=1, 
        on_delete=models.PROTECT
    )

class Client(models.Model):
    nom_client=models.CharField(max_length=50,null=False,blank=False)
    phone=models.CharField( max_length=25,null=True,blank=True,unique=True)
    User=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False, 
        default=1,
        on_delete=models.PROTECT
    )
    
class Facture(models.Model):
    numero = models.IntegerField(null=False, blank=False,unique=True)
    date_fact = models.DateField(auto_now_add=True)  # Enregistre la date de création
    client = models.ForeignKey(Client, default=0,null=False,on_delete=models.CASCADE)
    User=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False, 
        default=1,
        on_delete=models.PROTECT
    )

class Transation(models.Model):
    qt_trans = models.IntegerField(null=False, blank=False)
    date_trans = models.DateField(null=False,auto_now_add=True)  # Enregistre la date de création
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,null=False, on_delete=models.CASCADE)
    prix_unitaire = models.FloatField(null=False, blank=False)
    User=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False, 
        default=1,
        on_delete=models.PROTECT
    )