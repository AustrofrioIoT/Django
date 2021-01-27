from django.db import models
from embed_video.fields import EmbedVideoField


class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to="projects",verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=["-created"] #ordena segun fecha de creacion

    def __str__(self):
        return self.title


class Video(models.Model):
    video=EmbedVideoField()
