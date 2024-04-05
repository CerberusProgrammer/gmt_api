from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from trip.views import CasetaViewSet, RutaViewSet, VehiculoViewSet, ViajeViewSet

router = DefaultRouter()
router.register(r'viajes', ViajeViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'casetas', CasetaViewSet)
router.register(r'vehiculos', VehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]