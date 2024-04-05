from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.name} {self.cost}'

class Stand(models.Model):
    name = models.CharField(max_length=255)
    vehicles = models.ManyToManyField(Vehicle)
    
    def __str__(self):
        return f'{self.name}'

class Route(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    road = models.CharField(max_length=255)
    length = models.DecimalField(max_digits=10, decimal_places=3)
    time = models.CharField(max_length=255)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name} | {self.length} KM'

class Trip(models.Model):
    from_city = models.CharField(max_length=255)
    to_city = models.CharField(max_length=255)
    from_date = models.DateTimeField()
    routes = models.ManyToManyField(Route)

    def __str__(self):
        return f'{self.from_city} a {self.to_city}'