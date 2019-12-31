from django.urls import path
from produto.views import *

urlpatterns = [
    path('produtos/', ProdutoList.as_view(), name=ProdutoList.name),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name=ProdutoDetail.name),
    path('produtos/<int:pk>/update', ProdutoDetailDeleteUpdate.as_view(), name=ProdutoDetailDeleteUpdate.name),
    path('produtos/<int:pk>/delete', ProdutoDetailDeleteUpdate.as_view(), name=ProdutoDetailDeleteUpdate.name),
]
