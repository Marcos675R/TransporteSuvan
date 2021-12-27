from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
opciones_consultas = [
    [0, "Reserva Servicio"],
    [1, "Sugerencia"],
    [2, "Reclamo"],
    [3, "felicitaciones"]

]
class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField()
    tipo_consulta=models.IntegerField(choices= opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre

class Servicio (models.Model):
    tipoServicio = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.tipoServicio 

class Reservas (models.Model):
    nombreServicio = models.CharField(max_length=70)
    precio = models.IntegerField()
    descripcion = models.TextField()
    tipoServicio =models.ForeignKey(Servicio, on_delete = models.PROTECT)
    imagen = models.ImageField(upload_to="servicio", null= True)

    def __str__(self) -> str:
        return self.nombreServicio
