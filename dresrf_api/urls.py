from django.contrib import admin
from django.urls import path
from core.views import test_view, TestView
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('test/', test_view, name='test'),
    path('', TestView.as_view(), name='testview'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
]
