from django.db import models

class Trip(models.Model):
    CITIES = (
        ("MXL", "Mexicali"),
        ("TCT", "Tecate"),
        ("TIJ", "Tijuana"),
        ("RST", "Rosarito"),
        ("ENS", "Ensenada"),
    )
    
    VEHICLES = (
        ()
    )
    
    from_city = models.CharField(max_length=20, choices=CITIES)
    from_city_date = models.DateTimeField()
    to_city = models.CharField(max_length=20, choices=CITIES)
    to_city_data = models.DateTimeField()
    passengers = models.IntegerField()
    vehicle = models.CharField(max_length=100, choices=VEHICLES)
    toll = models.DecimalField()
    