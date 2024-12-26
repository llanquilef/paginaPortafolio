from django.db import models

class MultimediaFavorita(models.Model):
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    comentario = models.TextField(max_length=600)
    imagen = models.ImageField(upload_to='imgs/')
    fecha_publicacion = models.DateField()
    hora_publicacion = models.TimeField()
    TIPO_MULTIMEDIA = [
        ('Libro', 'Libro'),
        ('Película', 'Película'),
        ('Serie', 'Serie'),
        ('Albúm', 'Albúm'),
        ('Podcast', 'Podcast'),
        ('Cómic', 'Cómic'),
        ('Manga', 'Manga'),
    ]
    tipoMultimedia = models.CharField(max_length=50, choices=TIPO_MULTIMEDIA)

class RecomendacionUsuario(models.Model):
    nombre_recomendacion = models.CharField(max_length=150)
    autor_recomendacion = models.CharField(max_length=150)
    comentario_recomendacion = models.TextField(max_length=600)
    imagen_recomendacion = models.ImageField(upload_to='imgs/')
    fecha_recomendacion = models.DateField()
    hora_recomendacion = models.TimeField()
    TIPO_MULTIMEDIA = [
        ('Libro', 'Libro'),
        ('Película', 'Película'),
        ('Serie', 'Serie'),
        ('Albúm', 'Albúm'),
        ('Podcast', 'Podcast'),
        ('Cómic', 'Cómic'),
        ('Manga', 'Manga'),
    ]
    tipoMultimedia = models.CharField(max_length=50, choices=TIPO_MULTIMEDIA)
