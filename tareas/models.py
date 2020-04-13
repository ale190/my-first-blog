from django.db import models

class Tareas(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
