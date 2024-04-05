from django.db import models

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.nombre} {self.costo}'

class Caseta(models.Model):
    nombre = models.CharField(max_length=255)
    vehiculos = models.ManyToManyField(Vehiculo)
    
    def __str__(self):
        return f'{self.nombre}'

class Ruta(models.Model):
    nombreRuta = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    tipoCarretera = models.CharField(max_length=255)
    longitudKm = models.DecimalField(max_digits=10, decimal_places=3)
    tiempoEstimado = models.CharField(max_length=255)
    caseta = models.ForeignKey(Caseta, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombreRuta} | {self.longitudKm} KM'

class Viaje(models.Model):
    deCiudad = models.CharField(max_length=255)
    aCiudad = models.CharField(max_length=255)
    rutas = models.ManyToManyField(Ruta)

    def __str__(self):
        return f'{self.deCiudad} a {self.aCiudad}'