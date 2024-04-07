from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from trip.views import CasetaViewSet, RutaViewSet, VehiculoViewSet, ViajeViewSet

router = DefaultRouter()
router.register(r'trips', ViajeViewSet)
router.register(r'routes', RutaViewSet)
router.register(r'stands', CasetaViewSet)
router.register(r'vehicles', VehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]