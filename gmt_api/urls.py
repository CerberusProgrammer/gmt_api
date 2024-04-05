from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from trip.views import UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('trip.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('register/', UserCreate.as_view(), name='account_register'),
]
