from django.contrib import admin

from django.contrib import admin
from .models import Perfil, Habilidad, Experiencia, Educacion

admin.site.register(Perfil)
admin.site.register(Habilidad)
admin.site.register(Experiencia)
admin.site.register(Educacion)