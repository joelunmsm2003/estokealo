from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import *
from app.models import *
from django.forms import ModelForm, TextInput

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

class AutoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','subcategoria','auto','anio','kilometraje','color','cilindros','transmision','combustible','condicion','moneda','transaction','distrito','provincia','telefono')
        widgets = {
            'id':TextInput(attrs={'class':'form-control'}),
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'auto':TextInput(attrs={'class':'form-control'}),
            'anio':TextInput(attrs={'class':'form-control'}),
            'kilometraje':TextInput(attrs={'class':'form-control'}),
            'color':TextInput(attrs={'class':'form-control'}),
            'cilindros':TextInput(attrs={'class':'form-control'}),
            'transmision':TextInput(attrs={'class':'form-control'}),
            'combustible':TextInput(attrs={'class':'form-control'}),
            'condicion':TextInput(attrs={'class':'form-control'}),
            'transaction':TextInput(attrs={'class':'form-control'}),
            'distrito':TextInput(attrs={'class':'form-control'}),
            'provincia':TextInput(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control'}),
            'moneda':TextInput(attrs={'class':'form-control'})

        }


class PropiedadesForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','color','distrito','provincia','telefono','metros2','ubicacion','dormitorios','banios','piscina','jardin','amueblado','gimnasio','sauna','jacuzzi','ambientes')
        widgets = {
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'color':Select(attrs={'class':'form-control'}),
            'distrito':Select(attrs={'class':'form-control'}),
            'provincia':Select(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control'}),
            'metros2':TextInput(attrs={'class':'form-control'}),
            'ubicacion':TextInput(attrs={'class':'form-control'}),
            'dormitorios':TextInput(attrs={'class':'form-control'}),
            'banios':TextInput(attrs={'class':'form-control'}),
            'piscina':TextInput(attrs={'class':'form-control'}),
            'jardin':TextInput(attrs={'class':'form-control'}),
            'amueblado':TextInput(attrs={'class':'form-control'}),
            'gimnasio':TextInput(attrs={'class':'form-control'}),
            'sauna':TextInput(attrs={'class':'form-control'}),
            'jacuzzi':TextInput(attrs={'class':'form-control'}),
            'ambientes':TextInput(attrs={'class':'form-control'}),
        }


class TabletsForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','condicion')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'condicion':Select(attrs={'class':'form-control'}),
        }

class ElectronicosForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','condicion')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'condicion':Select(attrs={'class':'form-control'}),
        }


class CasaForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
        }

class ModaForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
        }

class ArteForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
        }

class MascotasForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','animal')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
        }

class EmpleosForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','distrito','provincia','experiencia','empleo')
        widgets={
            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'distrito':Select(attrs={'class':'form-control'}),
            'provincia':Select(attrs={'class':'form-control'}),
            'experiencia':TextInput(attrs={'class':'form-control'}),
            'empleo':Select(attrs={'class':'form-control'}),

        }

class CursosForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('id','categoria','subcategoria','titulo','descripcion','precio','curso')
        widgets={

            'categoria':Select(attrs={'class':'form-control'}),
            'subcategoria':Select(attrs={'class':'form-control'}),
            'titulo':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'precio':TextInput(attrs={'class':'form-control'}),
            'curso':Select(attrs={'class':'form-control'}),
        }


