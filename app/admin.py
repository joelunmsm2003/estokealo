from django.contrib import admin
from app.models import *
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



# @admin.register(Anio)
# class AnioAdmin(admin.ModelAdmin):
#     list_display = ('id_anio','anio_antig')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','icon','imagen')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('getcategoria','nombre')
    list_filter = ('categoria__nombre',)

    def getcategoria(self, obj):
		return obj.categoria.nombre


@admin.register(Empleo)
class EmpleoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','get_provincia')
	def get_provincia(self, obj):
		return obj.provincia.name


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','marca','modelo','descripcion','titulo','moneda')
    list_editable = ('moneda',)

    def marca(self, obj):
        if obj.auto:
            return obj.auto.marca.nombre

    def modelo(self, obj):
        if obj.auto:
            return obj.auto.modelo.nombre


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('id','marca','modelo')
    search_fields = ('id',)

    def marca(self, obj):
        if obj.marca:
            return obj.marca.nombre

    def modelo(self, obj):
        if obj.modelo:
            return obj.modelo.nombre
