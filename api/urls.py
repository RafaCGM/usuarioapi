from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import RegisterView, UserListView, UserDetailView

urlpatterns = [
    # Autenticação JWT
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # URIs
    path('registro/', RegisterView.as_view()),
    path('usuarios/', UserListView.as_view()),
    path('usuarios/<int:pk>/', UserDetailView.as_view()),
]
