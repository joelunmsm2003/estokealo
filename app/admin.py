from django.contrib import admin
from app.models import *
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



# @admin.register(Anio)
# class AnioAdmin(admin.ModelAdmin):
#     list_display = ('id_anio','anio_antig')

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('getcategoria','nombre')
    list_filter = ('categoria__nombre',)

    def getcategoria(self, obj):
		return obj.categoria.nombre


