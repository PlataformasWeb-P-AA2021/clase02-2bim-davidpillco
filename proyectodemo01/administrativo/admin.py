from django.contrib import admin

from administrativo.models import Provincia
# Register your models here.

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class ProvinciaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'capital_provincial', 'poblacion')
    search_fields = ('nombre', 'capital_provincial')

# admin.site.register se lo altera

admin.site.register(Provincia, ProvinciaAdmin)
