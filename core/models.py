from django.db import models
from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    titulo_principal = models.CharField(max_length=200)  # Ej: Estudiante Avanzada de Lic. en Ciencias de la Computación
    titulo_intermedio = models.CharField(max_length=200) # Ej: Técnica Universitaria en Programación
    sobre_mi = models.TextField()
    linkedin = models.URLField()
    github = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    CATEGORIA_CHOICES = [
        ('Lenguajes', 'Lenguajes de Programación'),
        ('Frameworks', 'Frameworks y Librerías'),
        ('Plataformas', 'Plataformas o Software'),
        ('Herramientas', 'Herramientas (Excel, Git, etc.)'),
    ]
    
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='Intermedio')
    # Agregamos la categoría
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='Lenguajes')
    
    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

class Experiencia(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actual = models.BooleanField(default=False)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

class Educacion(models.Model):
    titulo = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    en_curso = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

# Create your models here.
