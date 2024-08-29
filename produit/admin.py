from django.contrib import admin
from .models import Produit,Client,Facture,Transation



# Register your models here.
admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Facture)
admin.site.register(Transation)
