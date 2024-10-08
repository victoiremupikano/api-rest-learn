from django.urls import path
from . views import (
    # produit
    ProduitDetailView, 
    ProduitListCreateView,
    ProduitUpdateView,
    ProduitDeleteView,
    # client
    ClientDetailView, 
    ClientListCreateView,
    ClientUpdateView,
    ClientDeleteView,
    # facture
    FactureDetailView, 
    FactureListCreateView,
    FactureUpdateView,
    FactureDeleteView,

    # transaction 
    TransactionDetailView,
    TransactionListCreate,
    TransactionWithFactureListCreate,
    TransactionUpdateView,
    TransactionDeleteView
)

urlpatterns = [
    # prouit
    path('produit-detail/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('produit-list-create/', ProduitListCreateView.as_view(), name='produit-list-create'),
    path('produit-update/<int:pk>/', ProduitUpdateView.as_view(), name='produit-update'),
    path('produit-delete/<int:pk>/', ProduitDeleteView.as_view(), name='produit-delete'),
    # client
    path('client-detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client-list-create/', ClientListCreateView.as_view(), name='client-list-create'),
    path('client-update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('client-delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
    # facture
    path('facture-detail/<int:pk>/', FactureDetailView.as_view(), name='facture-detail'),
    path('facture-list-create/', FactureListCreateView.as_view(), name='facture-list-create'),
    path('facture-update/<int:pk>/', FactureUpdateView.as_view(), name='facture-update'),
    path('facture-delete/<int:pk>/', FactureDeleteView.as_view(), name='facture-delete'),
    # transaction 
    path('transaction-detail/<int:pk>/',TransactionDetailView.as_view(),name='transaction-detail'),
    path('transaction-list-create/',TransactionListCreate.as_view(),name='transaction-list-create'),
    path('transaction-list-with-facture/<int:facture_id>/',TransactionWithFactureListCreate.as_view(),name='transaction-list-with-facture'),
    path('transaction-update/<int:pk>/',TransactionUpdateView.as_view(),name='transaction-update-view'),
    path('transaction-delete/<int:pk>/',TransactionDeleteView.as_view(),name='transaction-delete')
]
