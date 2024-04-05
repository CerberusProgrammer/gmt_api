from django.contrib import admin

from trip.models import Caseta, Ruta, Vehiculo, Viaje

admin.site.register(Viaje)
admin.site.register(Vehiculo)
admin.site.register(Caseta)
admin.site.register(Ruta)