from django.urls import path
from authentication.views import (
    CustomTokenVerifyView,
    UserLoginView,
    UserChangePasswordView,
    UserDetailView,
    UserListCreateView,
    UserUpdateView,
    UserDeleteView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token-verify'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),

    path('user-detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user-list-create/', UserListCreateView.as_view(), name='user-list-create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
