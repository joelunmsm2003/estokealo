import django_filters
from app.models import *

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = {
            'titulo': ['contains'],
            'descripcion': ['contains'],


        }