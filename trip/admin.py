from django.contrib import admin

from trip.models import Stand, Route, Vehicle, Trip

admin.site.register(Trip)
admin.site.register(Vehicle)
admin.site.register(Stand)
admin.site.register(Route)