from django.urls import path
from compra.views import *

urlpatterns = [
    path('vendas/', CompraList.as_view(), name=CompraList.name),
    path('vendas/<int:pk>/', CompraDetail.as_view(), name=CompraDetail.name),
    path('vendas/<int:id_produto>/comprar/', ProdutoCompra.as_view(), name=ProdutoCompra.name),

]
