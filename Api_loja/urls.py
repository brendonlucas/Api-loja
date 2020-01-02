from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from usuario.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('usuario.urls')),
    url('', include('produto.urls')),
    url('', include('compra.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
