from django.db import models

# Create your models here
class Entrada(models.Model):
    
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    aidi = models.TextField(max_length=10)
    
    def __str__(self):
        return 'entrada: ' + self.nombre + ' el dia ' + self.fecha.strftime("%d/%m/%Y") + ' con id: ' + self.aidi