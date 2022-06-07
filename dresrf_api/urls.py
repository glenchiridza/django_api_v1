from django.contrib import admin
from django.urls import path
from core.views import test_view,TestView
from django.urls import include

urlpatterns = [
    path('api-auth',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('test',test_view,name='test'),
    path('',TestView.as_view(),name='testview')
]
