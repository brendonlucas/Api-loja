import rest_framework
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('', include('usuario.urls')),
    url('', include('produto.urls')),
    url('', include('compra.urls')),
]
