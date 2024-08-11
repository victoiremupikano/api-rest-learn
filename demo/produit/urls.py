from django.urls import path
from . views import (
    ProduitDetailView, 
    ProduitListCreateView,
    ProduitUpdateView,
    ProduitDeleteView
)

urlpatterns = [
    path('produit-detail/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('produit-list-create/', ProduitListCreateView.as_view(), name='produit-list-create'),
    path('produit-update/<int:pk>/', ProduitUpdateView.as_view(), name='produit-update'),
    path('produit-delete/<int:pk>/', ProduitDeleteView.as_view(), name='produit-delete')
]
