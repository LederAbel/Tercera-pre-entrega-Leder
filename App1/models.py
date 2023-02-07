from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(default="pedal@gmail.com")
    direccion = models.CharField(max_length=80)
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    
class StockPropio(models.Model):
    modelo = models.CharField(max_length=50)
    efecto = models.CharField(max_length=50)
    unidades = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.CharField(max_length=20)
    
   
class PedalReparar(models.Model):
    nombre = models.CharField(max_length=50) #Nombre del pedal
    efecto = models.CharField(max_length=50) #Tipo de Efecto
    fabricante = models.CharField(max_length=50)
    volts = models.CharField(max_length=20) #alimentacion
    made = models.CharField(max_length=50) #procedencia
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    presupuesto = models.IntegerField(default=6000)
    envio = models.CharField(max_length=10)
    
   
class PedalClon(models.Model):
    clon_de = models.CharField(max_length=80)
    mods = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    envio = models.BooleanField()
    precio = models.IntegerField()

class VentaPropio(models.Model):
    modelo = models.ForeignKey(StockPropio, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=None)
    precio = models.IntegerField(default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    envio = models.BooleanField(default=True)
    



      
      