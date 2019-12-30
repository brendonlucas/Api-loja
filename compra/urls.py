from django.urls import path
from compra.views import *

urlpatterns = [
    path('compras/', CompraList.as_view(), name=CompraList.name),
    path('compras/<int:pk>/', CompraDetail.as_view(), name=CompraDetail.name),
    path('compras/<int:id_produto>/comprar/', ProdutoCompra.as_view(), name=ProdutoCompra.name),

]
