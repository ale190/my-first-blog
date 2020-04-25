from django.db import models

class Tarea(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    comentarios = models.TextField()

    def __str__(self):
        return self.titulo
