from django.urls import path
from .views import(
    # views for pr oduit
    
    ProduitDetailView,
    ProduitListCreate,
    ProduitDeleteView,
    ProduitUpdateView,
    
    # views for customers
    
    ClientDetailView,
    ClientListCreate,
    ClientUpdateView,
    ClientDeleteView,
    
    # views for facture
    
    FactureDetailView,
    FactureListCreate,
    FactureUpdateView,
    FactureDeleteView,
    
    # views for transaction
    
    TransactionDetailView,
    TransactionListCreate,
    TransactionUpdateView,
    TransactionDeleteView
    
)

urlpatterns = [
    path('produit-detail/<int:pk>/',ProduitDetailView.as_view(),name='produit-detail'),
    path('produit-delete/<int:pk>/',ProduitDeleteView.as_view(),name='produit-delete'),
    path('produit-list-create/',ProduitListCreate.as_view(),name='produit-list-create'),
    path('produit-update-view/<int:pk>/',ProduitUpdateView.as_view(),name='produit-update-view'),
    
    # urls pour les vues de Client
    
    path('client-delete/<int:pk>/',ClientDeleteView.as_view(),name='client-delete'),
    path('client-list-create/',ClientListCreate.as_view(),name='client-list-create'),
    path('client-update-view/<int:pk>/',ClientUpdateView.as_view(),name='client-update-view'),
    path('client-detail-view/<int:pk>/',ClientDetailView.as_view(),name='client-detail-view'),
    
    # urls vues du facture
    
    path('Facture-detail/<int:pk>/',FactureDetailView.as_view(),name='Facture-detail'),
    path('Facture-list-create/',FactureListCreate.as_view(),name='Facture-list-create'),
    path('Facture-update-view/<int:pk>/',FactureUpdateView.as_view(),name='Facture-update-view'),
    path('Facture-delete/<int:pk>/',FactureDeleteView.as_view(),name='Facture-delete'),
    
    # urls vues des transactions
    
    path('Transaction-detail/<int:pk>/',TransactionDetailView.as_view(),name='Transaction-detail'),
    path('Transaction-list-create/',TransactionListCreate.as_view(),name='Transaction-list-create'),
    path('Transaction-update-view/<int:pk>/',TransactionUpdateView.as_view(),name='Transaction-update-view'),
    path('Transaction-delete/<int:pk>/',TransactionDeleteView.as_view(),name='Transaction-delete')
]
