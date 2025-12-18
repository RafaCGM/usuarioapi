from django.urls import path
from .views import ProdutoCreateView

urlpatterns = [
    path('produtos/', ProdutoCreateView.as_view()),
]
