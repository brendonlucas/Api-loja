from django.urls import path
from usuario.views import *

urlpatterns = [
    path('funcionarios/', FuncionarioList.as_view(), name=FuncionarioList.name),
    path('funcionarios/<int:pk>/', FuncionarioDetail.as_view(), name=FuncionarioDetail.name),
    path('funcionarios/add/', FuncinarioAdd.as_view(), name=FuncinarioAdd.name),
]
