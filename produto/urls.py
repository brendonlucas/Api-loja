from django.urls import path
from produto.views import *

urlpatterns = [
    path('produtos/', ProdutoList.as_view(), name=ProdutoList.name),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name=ProdutoDetail.name),
]
