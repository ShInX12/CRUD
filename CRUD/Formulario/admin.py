from django.contrib import admin

from .models import Persona, Mascota


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'genero')
    list_filter = ('genero', )
    search_fields = ('nombre', )

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'nombre', 'edad', 'especie', 'color')
    list_filter = ('especie', )
    search_fields = ('persona', 'nombre')
