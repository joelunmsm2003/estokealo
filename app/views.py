from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import *
from estokeate import settings
from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail

from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
import time
import collections
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
from PIL import Image
from resizeimage import resizeimage
from estokeate.settings import *
from datetime import datetime,timedelta
from django.contrib.auth import authenticate
import re
from django.contrib.sites.shortcuts import get_current_site

from .forms import *
from .filtros import *



def mobile(request):
	"""Return True if the request comes from a mobile device."""
	MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
		return True
	else:
		return False

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]

def home(request):

	user = request.user.id

	usuario = None

	productos= Producto.objects.all().order_by('-id')

	for p in productos:

		p.imagen1 = 'true'

		if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>0:

			p.photo = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').order_by('-id')[0]

			p.photo_home = p.photo['photo__photo'].split('.')[0]+'_home.jpg'

		if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>1:

			p.photo1 = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').order_by('-id')[1]

			p.photo_home1 = p.photo1['photo__photo'].split('.')[0]+'_home.jpg'

	if user:

		usuario= AuthUser.objects.get(id=user)

		if ('https://' in str(usuario.photo))==False:

			usuario.photo = str(host)+str(usuario.photo)

	categoria = Categoria.objects.all().values('id','nombre','icon','descripcion','imagen')

	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

		if f.photo.find(".jpg") !=-1:formato ='.jpg'
		if f.photo.find(".png") !=-1:formato ='.png'
		if f.photo.find(".gif") !=-1:formato ='.gif'

		f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'

	# Mensajes en el Header


	compradores = Chat.objects.filter(destino_id=user).annotate(count=Count('id'))

	propios = Chat.objects.filter(user_id=user).annotate(count=Count('producto'))

	compradores = ValuesQuerySetToDict(compradores)+ValuesQuerySetToDict(propios)

	## Mobile Detection
	m=None
	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'homemovil.html',{'favoritos':favoritos,'productos':productos,'usuario':usuario,'host':host,'categoria':categoria})

	else:	

		return render(request, 'home.html',{'favoritos':favoritos,'productos':productos,'usuario':usuario,'host':host,'categoria':categoria})


def autentificacion(request):

	m=None

	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'loginmovil.html',{'host':host})

	else:	

		return render(request, 'login.html',{'host':host})

@login_required(login_url="/autentificacion")

def editarproducto(request,id):

	if request.method == 'POST':


		print 'request.POST',request.POST,id

		nombre_categoria = Categoria.objects.get(id=request.POST['categoria']).nombre

		if nombre_categoria=='Vehiculos':
		
			form = AutoForm(request.POST)

		if nombre_categoria=='Propiedades':

			form = PropiedadesForm(request.POST)

		if nombre_categoria=='Telefonos-Tablets':

			form = TabletsForm(request.POST)

		if nombre_categoria=='Electronicos-Video':

			form = ElectronicosForm(request.POST)

		if nombre_categoria=='Casa-Muebles':

			form = CasaForm(request.POST)

		if nombre_categoria=='Moda-Belleza':

			form = ModaForm(request.POST)

		if nombre_categoria=='Arte':

			form = ArteForm(request.POST)

		if nombre_categoria=='Mascotas':

			form = MascotasForm(request.POST)

		if nombre_categoria=='Empleos y Servicios':

			form = EmpleosForm(request.POST)

		if nombre_categoria=='Clases Cursos':

			form = CursosForm(request.POST)


		if form.is_valid():

			a = Producto.objects.get(id=id)

			if nombre_categoria=='Vehiculos':
			
				form = AutoForm(request.POST, instance=a).save()

			if nombre_categoria=='Propiedades':

				form = PropiedadesForm(request.POST, instance=a).save()

			if nombre_categoria=='Telefonos-Tablets':

				form = TabletsForm(request.POST, instance=a).save()

			if nombre_categoria=='Electronicos-Video':

				form = ElectronicosForm(request.POST, instance=a).save()

			if nombre_categoria=='Casa-Muebles':

				form = CasaForm(request.POST, instance=a).save()

			if nombre_categoria=='Moda-Belleza':

				form = ModaForm(request.POST, instance=a).save()

			if nombre_categoria=='Arte':

				form = ArteForm(request.POST, instance=a).save()

			if nombre_categoria=='Mascotas':

				form = MascotasForm(request.POST, instance=a).save()

			if nombre_categoria=='Empleos y Servicios':

				form = EmpleosForm(request.POST, instance=a).save()

			if nombre_categoria=='Clases Cursos':

				form = CursosForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/editarproducto/'+str(id))

	else:

		_producto = Producto.objects.get(id=id)

		_categoria=_producto.categoria

		print '_categoria',_categoria

		if _categoria.nombre=='Vehiculos':
		
			form = AutoForm(instance=_producto)

		if _categoria.nombre=='Propiedades':

			form = PropiedadesForm(instance=_producto)

		if _categoria.nombre=='Telefonos-Tablets':

			form = TabletsForm(instance=_producto)

		if _categoria.nombre=='Electronicos-Video':

			form = ElectronicosForm(instance=_producto)

		if _categoria.nombre=='Casa-Muebles':

			form = CasaForm(instance=_producto)

		if _categoria.nombre=='Moda-Belleza':

			form = ModaForm(instance=_producto)

		if _categoria.nombre=='Arte':

			form = ArteForm(instance=_producto)

		if _categoria.nombre=='Mascotas':

			form = MascotasForm(instance=_producto)

		if _categoria.nombre=='Empleos y Servicios':

			form = EmpleosForm(instance=_producto)

		if _categoria.nombre=='Clases Cursos':

			form = CursosForm(instance=_producto)


		
		return render(request, 'editarproducto.html',{'form':form,'producto':_producto})



@login_required(login_url="/autentificacion")

def salir(request):

	logout(request)
	
	return HttpResponseRedirect("/")



@login_required(login_url="/autentificacion")

def eliminarproducto(request,id):

	

	f =Favoritoproducto.objects.filter(producto_id=id)
	
	for fa in f:
		fa.delete()

	Producto.objects.get(id=id).delete()

	return HttpResponseRedirect("/productos/"+str(request.user.id))


@login_required(login_url="/autentificacion")
def perfil(request):

	user = request.user.id

	productos= Producto.objects.filter(user_id=user)

	usuario= AuthUser.objects.get(id=user)

	if ('https://' in str(usuario.photo))==False:

		usuario.photo = str(host)+str(usuario.photo)

	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']


	m=None
	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'perfilmovil.html',{'favoritos':favoritos,'productos':productos,'usuario':usuario,'miperfil':'active','host':host})

	else:	

		return render(request, 'perfil.html',{'favoritos':favoritos,'productos':productos,'usuario':usuario,'miperfil':'active','host':host})

@login_required(login_url="/autentificacion")
def favoritos(request):

	user = request.user.id

	productos= Producto.objects.filter(user_id=user)

	usuario= AuthUser.objects.get(id=user)

	if ('https://' in str(usuario.photo))==False:

		usuario.photo = str(host)+str(usuario.photo)

	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

		if f.photo.find(".jpg") !=-1:formato ='.jpg'
		if f.photo.find(".png") !=-1:formato ='.png'
		if f.photo.find(".gif") !=-1:formato ='.gif'

		f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'





	m=None
	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'favoritosmovil.html',{'favoritos':favoritos,'productos':productos,'usuario':usuario,'miperfil':'active','host':host})

	else:	

		return render(request, 'favoritos.html',{'favoritos':favoritos,'productos':productos,'usuario':usuario,'miperfil':'active','host':host})




@login_required(login_url="/autentificacion")

def actualizaperfil(request):


	if request.method == 'POST':

		user = request.user.id

		direccion = None

		nombre=None

		telefono= None


		productos= Producto.objects.filter(user_id=user)

		usuario= AuthUser.objects.get(id=user)

		username = request.POST['username']
		
		direccion = request.POST['direccion']

		telefono = request.POST['telefono']

		nombre = request.POST['nombre']

		for p in request.FILES:

			if p == 'photo':

				photo =  request.FILES['photo']

				u = AuthUser.objects.get(id=user)

				u.photo=photo

				u.save()


		u = AuthUser.objects.get(id=user)

		u.direccion = direccion

		u.first_name = nombre

		u.telefono=telefono

		u.save()


		for p in request.FILES:

			if p == 'photo':

				caption = '/home/estokeate/'+str(u.photo)

				fd_img = open(caption, 'r')

				img = Image.open(fd_img)

				width, height = img.size

				

				img = resizeimage.resize_cover(img, [200, 200])

				img.save(caption, img.format)

				fd_img.close()


		return HttpResponseRedirect("/perfil/")

def filtrarcategoria(request,dato,categoria):



	precio='precio'

	vista='listado'

	print '.....',request.get_full_path()

	if len(request.get_full_path().split('&'))>1:

		if 'listado' in request.get_full_path(): vista = 'listado'
		if 'galeria' in request.get_full_path(): vista = 'galeria'
		if 'precio' in request.get_full_path(): precio  = 'precio'
		if '-precio' in request.get_full_path(): precio  = '-precio'


	dato_1 = dato

	dato = dato.replace('_',' ')

	user = request.user.id

	if precio=='null':

		precio='precio'

	productos= Producto.objects.filter(descripcion__contains=dato,categoria_id=categoria).order_by(precio)
 
	subcat = Subcategoria.objects.filter(categoria_id=categoria)

	cat = Categoria.objects.get(id=categoria)

	resultados= Producto.objects.filter(descripcion__contains=dato,categoria_id=categoria).values('subcategoria','subcategoria__nombre').annotate(total=Count('subcategoria'))



	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

	for p in productos:

		if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>0:

			p.photo = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo')[0]



	return render(request, 'filtrasubcategoria.html',{'vista':vista,'dato_1':dato_1,'host':host,'productos':productos,'dato':dato,'subcat':subcat,'categoria':cat,'resultados':resultados,'totalcat':productos.count()})

def filtrarsubcategoria(request,dato,subcategoria):


	precio='precio'

	vista='listado'

	if 'listado' in request.get_full_path(): vista = 'listado'
	if 'galeria' in request.get_full_path(): vista = 'galeria'
	if 'precio' in request.get_full_path(): precio  = 'precio'
	if '-precio' in request.get_full_path(): precio  = '-precio'

	if precio=='null':

		preico='precio'

	dato_1=dato

	dato = dato.replace('_',' ')

	user = request.user.id

	productos= Producto.objects.filter(descripcion__contains=dato,subcategoria_id=subcategoria).order_by(precio)
 
	subcat = Subcategoria.objects.get(id=subcategoria)

	cat = Categoria.objects.get(id=subcat.categoria.id)

	totalcat = Producto.objects.filter(descripcion__contains=dato,categoria_id=cat.id).count()
 
	resultados= Producto.objects.filter(descripcion__contains=dato,categoria_id=cat.id).values('subcategoria','subcategoria__nombre').annotate(total=Count('subcategoria'))

	
	#All

	if dato =='all':

		productos= Producto.objects.filter(subcategoria_id=subcategoria)

		subcat = Subcategoria.objects.get(id=subcategoria)

		cat = Categoria.objects.get(id=subcat.categoria.id)

		totalcat = Producto.objects.filter(categoria_id=cat.id).count()

		resultados= Producto.objects.filter(categoria_id=cat.id).values('subcategoria','subcategoria__nombre').annotate(total=Count('subcategoria'))






	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

	for p in productos:

		if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>0:

			p.photo = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo')[0]



	return render(request, 'resultadosubcategoria.html',{'vista':vista,'host':host,'dato_1':dato_1,'productos':productos,'dato':dato,'subcat':subcat,'categoria':cat,'resultados':resultados,'totalsubcat':productos.count(),'totalcat':totalcat})



@csrf_exempt
def enviarnotis(request,id):



	if request.method == 'POST':

		body= json.loads(request.body)['body']

		title= json.loads(request.body)['title']

		photo = json.loads(request.body)['photo']

		photo_user = json.loads(request.body)['photo_user']

		data = simplejson.dumps(body)

	if int(id)==0:

		n=Notificacion.objects.get(user_id__isnull=True)

	else:

		n=Notificacion.objects.get(user_id=id)


	print 'n.payload',n.payload

	endpoint= n.endpoint

	auth= n.auth
	p256dh =n.p256dh



	os.system('python /home/estokeate/envia.py '+str(endpoint)+' '+str(auth)+' '+str(p256dh)+' "'+str(body)+'" "'+str(title)+'" "'+str(photo)+'" "'+str(photo_user)+'"')

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def recibenotis(request):

	user = request.user.id

	data = request.POST['keys']

	endpoint = json.loads(data)['endpoint']

	data = json.loads(data)['keys']

	f = open('/home/estokeate/notificaciones.txt', 'a')
	f.write('p256dh.bsbsbsbsbsb...'+str(user)+'\n')
	f.close()

	Notificacion.objects.filter(user_id=user).delete()

	Notificacion(payload=data,auth=data['auth'],endpoint=endpoint,p256dh=data['p256dh'],user_id=user).save()




	# f = open('/home/estokeate/notificaciones.txt', 'a')
	# f.write(str(data)+'\n')
	# f.close()

	return render(request, 'home.html',{}) 

@login_required(login_url="/autentificacion")
def chat(request,id_user,id_producto):

	user = request.user.id

	productos= Producto.objects.filter(user_id=user)




	usuario= AuthUser.objects.get(id=user)

	if ('https://' in str(usuario.photo))==False:

		usuario.photo = str(host)+str(usuario.photo)

	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

		if f.photo.find(".jpg") !=-1:formato ='.jpg'
		if f.photo.find(".png") !=-1:formato ='.png'
		if f.photo.find(".gif") !=-1:formato ='.gif'
		
		f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'


	m=None
	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'chatmovil.html',{'host':host,'productos':productos,'usuario':usuario,'mimensaje':'active'})

	else:

		return render(request, 'chat.html',{'id_user':id_user,'id_producto':id_producto,'favoritos':favoritos,'host':host,'productos':productos,'usuario':usuario,'mimensaje':'active'})




	
# Prductos de un usuario

@login_required(login_url="/autentificacion/")

def productos(request,id):

	user = request.user.id

	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

		if ('https://' in str(usuario.photo))==False:

			usuario.photo = str(host)+str(usuario.photo)

	productos= Producto.objects.filter(user_id=id)

	for p in productos:

		if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>0:

			p.photo = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo')[0]['photo__photo']

			if p.photo.find(".jpg") !=-1:formato ='.jpg'
			if p.photo.find(".png") !=-1:formato ='.png'
			if p.photo.find(".gif") !=-1:formato ='.gif'

			p.photo = p.photo.split(formato)[0]+'_thumbail.jpg'




	userproducto = AuthUser.objects.get(id=id)

	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

		if f.photo.find(".jpg") !=-1:formato ='.jpg'
		if f.photo.find(".png") !=-1:formato ='.png'
		if f.photo.find(".gif") !=-1:formato ='.gif'

		f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'


	m=None
	if mobile(request):
		m='m'


	if m=='m':	

		return render(request, 'productosusermovil.html',{'favoritos':favoritos,'host':host,'userproducto':userproducto,'productos':productos,'usuario':usuario,'mianuncio':'active'})

	else:	

		return render(request, 'productosuser.html',{'favoritos':favoritos,'host':host,'userproducto':userproducto,'productos':productos,'usuario':usuario,'mianuncio':'active'})

# Prductos de un usuario

@login_required(login_url="/autentificacion/")

def productosamostrar(request,id):

	user = request.user.id

	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

		if ('https://' in str(usuario.photo))==False:

			usuario.photo = str(host)+str(usuario.photo)

	productos= Producto.objects.filter(user_id=id)

	for p in productos:

		if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>0:

			p.photo = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo')[0]['photo__photo']

			if p.photo.find(".jpg") !=-1:formato ='.jpg'
			if p.photo.find(".png") !=-1:formato ='.png'
			if p.photo.find(".gif") !=-1:formato ='.gif'

			p.detalle = p.photo.split(formato)[0]+'_thumbail.jpg'




	userproducto = AuthUser.objects.get(id=id)

	m=None
	if mobile(request):
		m='m'


	if m=='m':	

		return render(request, 'productosusermovilamostrar.html',{'host':host,'userproducto':userproducto,'productos':productos,'usuario':usuario,'mianuncio':'active'})

	else:	

		return render(request, 'productosuseramostrar.html',{'host':host,'userproducto':userproducto,'productos':productos,'usuario':usuario,'mianuncio':'active'})




def clasificados(request):

	autos= Subcategoria.objects.filter(categoria_id=1)

	propiedades= Subcategoria.objects.filter(categoria_id=2)

	empleos= Subcategoria.objects.filter(categoria_id=9)

	user = request.user.id

	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

		if ('https://' in str(usuario.photo))==False:

			usuario.photo = str(host)+str(usuario.photo)


	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

		if f.photo.find(".jpg") !=-1:formato ='.jpg'
		if f.photo.find(".png") !=-1:formato ='.png'
		if f.photo.find(".gif") !=-1:formato ='.gif'

		f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'



	return render(request, 'clasificados.html',{'host':host,'usuario':usuario,'autos':autos,'propiedades':propiedades,'empleos':empleos})
	

def prueba(request):




	return render(request, 'productos.html',{'host':host})





# Prductos de un usuario

@login_required(login_url="/autentificacion")
def detallechat(request,user,producto):

	usuario_receptor= AuthUser.objects.get(id=user)

	user_id = request.user.id

	favorito = None

	if user_id:

		usuario =AuthUser.objects.get(id=user_id)

		if ('https://' in str(usuario.photo))==False:

			usuario.photo = str(host)+str(usuario.photo)



	if Favoritoproducto.objects.filter(user_id=user_id,producto_id=producto):

		favorito = Favoritoproducto.objects.get(user_id=user_id,producto_id=producto).estado

	return render(request, 'detallechat.html',{'favorito':favorito,'host':host,'user':user,'producto':producto,'usuario_receptor':usuario_receptor,'usuario':usuario})


# Prductos de un usuario
def detallechatpc_1(request,user):

	return HttpResponseRedirect("/")


#@login_required(login_url="/autentificacion")
def detallechatpc(request,user,id_producto):

	# user=None

	# if int(user)!=1:

	# 	user= Producto.objects.get(id=producto).user.id

	user = Producto.objects.get(id=id_producto).user.id

	
	if int(user)!=1:


		usuario_receptor= AuthUser.objects.get(id=user)

		usuario = None

		producto= Producto.objects.get(id=id_producto)

		videos = None

		favorito = None

		if Videoproducto.objects.filter(producto_id=id_producto):

			videos = Videoproducto.objects.filter(producto_id=id_producto)[0]

		user_id = request.user.id

		favoritos = Favoritoproducto.objects.filter(user_id=user_id)[:6]

		for f in favoritos:

			f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

			if f.photo.find(".jpg") !=-1:formato ='.jpg'
			if f.photo.find(".png") !=-1:formato ='.png'
			if f.photo.find(".gif") !=-1:formato ='.gif'

			f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'


		if user_id:

			usuario =AuthUser.objects.get(id=user_id)

			if ('https://' in str(usuario.photo))==False:

				usuario.photo = str(host)+str(usuario.photo)

			if Favoritoproducto.objects.filter(user_id=user_id,producto_id=id_producto).count()>0:

				favorito = Favoritoproducto.objects.get(user_id=user_id,producto_id=id_producto).estado
		
			return render(request, 'detallechatpc.html',{'favoritos':favoritos,'videos':videos,'host':host,'user':user,'producto':producto,'usuario_receptor':usuario_receptor,'usuario':usuario})

		else:

			return render(request, 'detallechatpc.html',{'videos':videos,'host':host,'user':user,'producto':producto,'usuario_receptor':usuario_receptor,'usuario':usuario})

	else:

		return HttpResponseRedirect("/")


def provincias(request):


	print 'ququuquq'

	p = Provincia.objects.all().values('id','name','orden').order_by('-orden')



	p = ValuesQuerySetToDict(p)

	p = simplejson.dumps(p)

	return HttpResponse(p, content_type="application/json")


def misfavoritos(request):

	user_id = request.user.id

	f = Favoritoproducto.objects.filter(user_id=user_id).values('producto__titulo')



	f = ValuesQuerySetToDict(f)

	f = simplejson.dumps(f)

	return HttpResponse(f, content_type="application/json")

def marcas(request):

	f = Marca.objects.all().values('id','nombre')

	f = ValuesQuerySetToDict(f)

	f = simplejson.dumps(f)

	return HttpResponse(f, content_type="application/json")




def distritos(request,provincia):

	f = Distrito.objects.filter(provincia_id=provincia).values('id','nombre')

	f = ValuesQuerySetToDict(f)

	f = simplejson.dumps(f)

	return HttpResponse(f, content_type="application/json")

def colores(request):

	f = Color.objects.all().values('id','nombre')

	f = ValuesQuerySetToDict(f)

	f = simplejson.dumps(f)

	return HttpResponse(f, content_type="application/json")



def modelos(request,marca):

	f = Auto.objects.filter(marca_id=marca).values('id','modelo__nombre','modelo')

	f = ValuesQuerySetToDict(f)

	f = simplejson.dumps(f)

	return HttpResponse(f, content_type="application/json")


def tipos(request,modelo):

	f = Auto.objects.filter(modelo_id=modelo).values('id','tipo__nombre','tipo')

	f = ValuesQuerySetToDict(f)

	f = simplejson.dumps(f)

	return HttpResponse(f, content_type="application/json")


def estadofavorito(request,producto):

	user_id = request.user.id

	favorito = None

	if user_id and Favoritoproducto.objects.filter(user_id=user_id,producto_id=producto):

		favorito = Favoritoproducto.objects.get(user_id=user_id,producto_id=producto).estado

	favorito = simplejson.dumps(favorito)
	

	return HttpResponse(favorito, content_type="application/json")

# Prductos de un usuario

def productosjson(request):

	productos_ = Producto.objects.all().values('id','categoria__nombre','precio','moneda','subcategoria__nombre','titulo','user','user__photo','user__first_name','user__username','user__telefono','descripcion')

	for p in range(len(productos_)):

		productos_[p]['photo'] = ValuesQuerySetToDict(Photoproducto.objects.filter(producto_id=productos_[p]['id']).values('id','photo__photo'))



	productos_ = ValuesQuerySetToDict(productos_)

	productos_ = simplejson.dumps(productos_)
	

	return HttpResponse(productos_, content_type="application/json")

# Busqueda por categoria

def busquedacategoria(request,categoria,subcategoria):


	vista='listado'

	precio='precio'

	print 'request.get_full_path()',request.get_full_path()

	if 'listado' in request.get_full_path(): vista = 'listado'
	if 'galeria' in request.get_full_path(): vista = 'galeria'
	if 'precio' in request.get_full_path(): precio  = 'precio'
	if '-precio' in request.get_full_path(): precio  = '-precio'

	usuario = None

	user=request.user.id

	if user:

		usuario =AuthUser.objects.get(id=user)

	if precio=='null':

		precio ='precio'

	if int(subcategoria)==0:

		producto = Producto.objects.filter(categoria_id=categoria).values('id','titulo','descripcion','precio','user_id').order_by(precio)

		cat = Categoria.objects.get(id=categoria)

	if int(categoria)==0:
	
		producto = Producto.objects.filter(subcategoria_id=subcategoria).values('id','titulo','descripcion','precio','user_id').order_by(precio)

		cat = Subcategoria.objects.get(id=subcategoria)


	resultados= Producto.objects.filter(categoria_id=categoria).values('subcategoria','subcategoria__nombre').annotate(total=Count('subcategoria'))


	favoritos = Favoritoproducto.objects.filter(user_id=user)

	for f in favoritos:

		f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

		if f.photo.find(".jpg") !=-1:formato ='.jpg'
		if f.photo.find(".png") !=-1:formato ='.png'
		if f.photo.find(".gif") !=-1:formato ='.gif'

		f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'

	for p in range(len(producto)):

		if Photoproducto.objects.filter(producto_id=producto[p]['id']).values('photo','photo__photo').count()>0:
		
			producto[p]['detalle'] = Photoproducto.objects.filter(producto_id=producto[p]['id']).values('photo','photo__photo')[0]['photo__photo']


	total = producto.count()

	print 'vista',vista

	m=None
	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'busquedacategoriamovil.html',{'favoritos':favoritos,'usuario':usuario,'resultados':resultados,'host':host,'productos':producto,'total':total,'categoria':cat})

	else:	

		return render(request, 'busquedacategoria.html',{'favoritos':favoritos,'usuario':usuario,'vista':vista,'resultados':resultados,'host':host,'productos':producto,'total':total,'categoria':cat})




def detalleproducto(request,id):

	producto = Producto.objects.filter(id=id).values('id','titulo','descripcion','precio','user__first_name','user__photo','user_id')

	for p in range(len(producto)):

		if ('https://' in str(producto[p]['user__photo']))==False:

			producto[p]['user__photo'] = str(host)+str(producto[p]['user__photo'])
		
		producto[p]['photo_producto'] = str(Photoproducto.objects.filter(producto_id=producto[p]['id']).values('photo','photo__photo')[0]['photo__photo'])



	producto = ValuesQuerySetToDict(producto)

	producto = simplejson.dumps(producto)

	return HttpResponse(producto, content_type="application/json")




# Productos por categoria

def productocategoria(request,id):

	producto = Producto.objects.filter(categoria_id=id).values('id','titulo','descripcion','precio')

	for p in range(len(producto)):

		producto[p]['detalle'] = str(Photoproducto.objects.filter(producto_id=producto[p]['id']).values('photo','photo__photo')[0]['photo__photo'])



	producto = ValuesQuerySetToDict(producto)

	producto = simplejson.dumps(producto)

	return HttpResponse(producto, content_type="application/json")


# MEsajes

def ordenar(data):
		 
	return data['id']

# Compradores de un usuario

@login_required(login_url="/autentificacion/")

def chatin(request,id):

	user = request.user.id

	compradores = Chat.objects.filter(destino_id=user).values('user','user__first_name','user__username','user__photo','producto','producto__titulo','producto__precio','producto__titulo').annotate(count=Count('id'))

	for p in range(len(compradores)):

		if ('https://' in str(compradores[p]['user__photo']))==False:

			compradores[p]['user__photo'] = str(host)+str(compradores[p]['user__photo'])

	propios = Chat.objects.filter(user_id=user).values('user','user__first_name','user__username','user__photo','producto','producto__titulo','producto__precio','producto__titulo').annotate(count=Count('producto'))


	for p in range(len(propios)):

		if ('https://' in str(propios[p]['user__photo']))==False:

			propios[p]['user__photo'] = str(host)+str(propios[p]['user__photo'])



	compradores = ValuesQuerySetToDict(compradores)+ValuesQuerySetToDict(propios)

	

	compradores = simplejson.dumps(compradores)

	return HttpResponse(compradores, content_type="application/json")



# Compradores de un usuario

@login_required(login_url="/autentificacion/")

def chatin2(request,id):

	user = request.user.id

	compradores = Chat.objects.filter(destino_id=user).values('user','user__first_name','user__username','user__photo','producto','producto__titulo','producto__precio','producto__titulo').annotate(count=Count('id')).order_by('-id')

	for p in range(len(compradores)):

		if ('https://' in str(compradores[p]['user__photo']))==False:

			compradores[p]['user__photo'] = str(host)+str(compradores[p]['user__photo'])

	propios = Chat.objects.filter(user_id=user).values('user','user__first_name','user__username','user__photo','producto','producto__titulo','producto__precio','producto__titulo').annotate(count=Count('producto')).order_by('-id')


	for p in range(len(propios)):

		if ('https://' in str(propios[p]['user__photo']))==False:

			propios[p]['user__photo'] = str(host)+str(propios[p]['user__photo'])



	compradores = ValuesQuerySetToDict(compradores)+ValuesQuerySetToDict(propios)

	

	compradores = simplejson.dumps(compradores)

	return HttpResponse(compradores, content_type="application/json")



@login_required(login_url="/autentificacion/")

def listamensajes(request,user,producto):

	destino = request.user.id

	# Mensajes que le llegan al dueno del producto

	mensajes = Chat.objects.filter(destino_id=destino,user_id=user,producto_id=producto).values('user__first_name','id','producto','producto__precio','destino','user','destino__username','user__username','user__photo','mensaje','producto__titulo','producto__categoria','producto__user__first_name')

	fmt = '%Y-%m-%d %H:%M:%S'

	for p in range(len(mensajes)):

		if ('https://' in str(mensajes[p]['user__photo']))==False:

			mensajes[p]['user__photo'] = str(host)+str(mensajes[p]['user__photo'])

		if Chat.objects.filter(id=mensajes[p]['id']).values('fecha')[0]['fecha']:

			mensajes[p]['fecha'] = Chat.objects.get(id=mensajes[p]['id']).fecha.strftime(fmt)
	
		mensajes[p]['photo_producto'] = str(Photoproducto.objects.filter(producto_id=mensajes[p]['producto'])[0].photo.photo)
		
	# Mensajes que envia el dueno del producto al interesado

	mensajes1 = Chat.objects.filter(destino_id=user,user_id=destino,producto_id=producto).values('user__first_name','id','producto','producto__precio','destino','user','destino__username','user__username','user__photo','mensaje','producto__titulo','producto__categoria','producto__user__first_name')

	fmt = '%Y-%m-%d %H:%M:%S'

	for p in range(len(mensajes1)):

		if ('https://' in str(mensajes1[p]['user__photo']))==False:

			mensajes1[p]['user__photo'] = str(host)+str(mensajes1[p]['user__photo'])

		if Chat.objects.filter(id=mensajes1[p]['id']).values('fecha')[0]['fecha']:

			mensajes1[p]['fecha'] = Chat.objects.get(id=mensajes1[p]['id']).fecha.strftime(fmt)
	
		mensajes1[p]['photo_producto'] = str(Photoproducto.objects.filter(producto_id=mensajes1[p]['producto'])[0].photo.photo)
		
	mensajes = ValuesQuerySetToDict(mensajes) + ValuesQuerySetToDict(mensajes1)

	mensajes = sorted(mensajes,key=ordenar)

	mensajes = simplejson.dumps(mensajes)

	return HttpResponse(mensajes, content_type="application/json")



def producto(request,id):

	user = request.user.id

	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

		if ('https://' in str(usuario.photo))==False:

			usuario.photo = str(host)+str(usuario.photo)

	producto= Producto.objects.get(id=id)

	if ('https://' in str(producto.user.photo))==False:

		producto.user.photo = str(host)+str(producto.user.photo)

	videos = None

	if Videoproducto.objects.filter(producto_id=id):

		videos = Videoproducto.objects.filter(producto_id=id)[0]

	m=None
	if mobile(request):
		m='m'

	if m=='m':	

		return render(request, 'productodetallemovil.html',{'host':host,'producto':producto,'usuario':usuario,'videos':videos})

	else:	

		return render(request, 'productodetalle.html',{'host':host,'producto':producto,'usuario':usuario,'videos':videos})



#Filtros



def search(request):
    user_list = Producto.objects.all()

    print 'user_list',user_list
    print 'request.GET',request.GET
    user_filter = ProductoFilter(request.GET, queryset=user_list)

    print 'user_filter',user_filter
    return render(request, 'busqueda.html', {'filter': user_filter})


def busqueda(request):

	categoria = Categoria.objects.all()

	precio='precio'

	vista='listado'

	print request.get_full_path()

	if len(request.get_full_path().split('&'))>1:

		if len(request.get_full_path().split('&vista='))>1:

			vista = request.get_full_path().split('&vista=')[1]

		if len(request.get_full_path().split('&precio='))>1:

			precio = request.get_full_path().split('&precio=')[1]


	if request.method == 'GET':


		#Filtros

		for r in request.GET:

			if r=='dato':
		
				dato= request.GET['dato']

			if r=='vista':

				vista =request.GET['vista']


		dato_1 = dato.replace(' ','_')

		user = request.user.id

		usuario = None

		if user:

			usuario =AuthUser.objects.get(id=user)

		categoria = Categoria.objects.all()

		print 'precio...',precio

		if precio == 'null':

			precio='precio' 
			
		productos = Producto.objects.filter(descripcion__contains=dato).order_by(precio)

		f = ProductoFilter(request.GET, queryset=productos)


		total = productos.count()

		for p in productos:

			if Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo').count()>0:

				p.photo = Photoproducto.objects.filter(producto_id=p.id).values('id','photo__photo')[0]


		resultados= Producto.objects.filter(descripcion__contains=dato).values('categoria','categoria__nombre','categoria__icon').annotate(total=Count('categoria'))

		m=None

		categoria = Categoria.objects.all()

		favoritos = Favoritoproducto.objects.filter(user_id=user)

		for f in favoritos:

			f.photo = Photoproducto.objects.filter(producto_id=f.producto.id).values('photo__photo')[0]['photo__photo']

			if f.photo.find(".jpg") !=-1:formato ='.jpg'
			if f.photo.find(".png") !=-1:formato ='.png'
			if f.photo.find(".gif") !=-1:formato ='.gif'

			f.photo = f.photo.split(formato)[0]+'_thumbail.jpg'




		if mobile(request):

			m='m'


		if m=='m':	

			return render(request, 'busquedamovil.html',{'favoritos':favoritos,'usuario':usuario,'categoria':categoria,'filter':f,'host':host,'categoria':categoria,'productos':productos,'total':total,'dato':dato,'resultados':resultados})

		else:	

			return render(request, 'busqueda.html',{'favoritos':favoritos,'usuario':usuario,'vista':vista,'dato_1':dato_1,'categoria':categoria,'filter':f,'host':host,'categoria':categoria,'productos':productos,'total':total,'dato':dato,'resultados':resultados})



def productojson(request,id):


	user = request.user.id

	usuario = None

	if user:

		usuario =AuthUser.objects.get(id=user)

	
	photos = Photoproducto.objects.filter(producto_id=id).values('id','photo__photo')

	for p in range(len(photos)):

		pho = str(Photoproducto.objects.get(id=photos[p]['id']).photo.photo)

		if pho.find(".jpg") !=-1:formato ='.jpg'
		if pho.find(".png") !=-1:formato ='.png'
		if pho.find(".gif") !=-1:formato ='.gif'


		photos[p]['detalle'] = pho.split(formato)[0]+'_thumbail.jpg'


	videos = Videoproducto.objects.filter(producto_id=id).values('id','video__video')

	photos = ValuesQuerySetToDict(photos)

	photos = simplejson.dumps(photos)
	

	return HttpResponse(photos, content_type="application/json")

@login_required(login_url="/autentificacion/")

def usuario(request,id):

	user = request.user.id

	usuario= AuthUser.objects.get(id=user)

	return render(request, 'usuario.html',{'host':host,'usuario':usuario})



def registra(request):

	if request.method == 'POST':


		user = request.POST['username']
		
		psw = request.POST['password']

		rpsw = request.POST['password']

		if psw == rpsw:

			User.objects.create_user(user, user, psw)

			user = authenticate(username=user, password=psw)


	return render(request, 'perfil.html')



@login_required(login_url="/autentificacion/")

def enviamensaje(request):

	if request.method == 'POST':

		user = request.user.id

		url = 'https://m.estokealo.com/enviarnotis/'

		first_name = AuthUser.objects.get(id=user).first_name

		fecha = datetime.today()-timedelta(hours=5)

		producto = request.POST['producto']

		mensaje = request.POST['mensaje']

		receptor = Producto.objects.get(id=producto).user.id

		data = {'title':'Mensaje de '+first_name,'body':mensaje}
        
		r = requests.post(url+str(receptor), data=json.dumps(data), headers=headers)

		Chat(user_id=user,destino_id=receptor,mensaje=mensaje,producto_id=producto,fecha=fecha).save()

		return HttpResponseRedirect("/producto/"+producto)

@csrf_exempt
def enviamensaje_perfil(request):

	if request.method == 'POST':

		user = request.user.id

		first_name = AuthUser.objects.get(id=user).first_name

		photo_user= str(AuthUser.objects.get(id=user).photo)

		if ('https://' in str(photo_user))==False:

			photo_user = str(host)+str(photo_user)

		url = 'https://m.estokealo.com/enviarnotis/'

		headers = {'Content-Type': 'application/json'}

		data = json.loads(request.body)

		fecha = datetime.today()-timedelta(hours=5)

		producto = data['producto']

		photo = host+str(Photoproducto.objects.filter(producto_id=producto)[0].photo.photo)

		mensaje = data['mensaje1']

		receptor = data['user']

		noti = {'body':mensaje,'title':'Mensaje de '+str(first_name),'photo':photo,'photo_user':photo_user}

		r = requests.post(url+str(receptor), data=json.dumps(noti), headers=headers)

		Chat(user_id=user,destino_id=receptor,mensaje=mensaje,producto_id=producto,fecha=fecha).save()

		data = simplejson.dumps(data)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def enviamensaje_perfil_web(request):

	if request.method == 'POST':

		user = request.user.id
		
		data = json.loads(request.body)['dato']

		fecha = datetime.today()-timedelta(hours=5)

		producto = data['producto']

		mensaje = data['mensaje1x']

		receptor = data['user']

		Chat(user_id=user,destino_id=receptor,mensaje=mensaje,producto_id=producto,fecha=fecha).save()

		data = simplejson.dumps(data)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarphoto(request,id):

	producto = Photoproducto.objects.get(photo_id=id).producto.id

	Photoproducto.objects.get(photo_id=id).delete()

	Photo.objects.get(id=id).delete()

	return HttpResponseRedirect("/editarproducto/"+str(producto))



@csrf_exempt
def noti(request):

	if request.method == 'POST':

		data = simplejson.dumps('subcategorias')

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def traesubcategorias(request,categoria):

	subcategorias = Subcategoria.objects.filter(categoria_id=categoria).values('id','nombre')

	subcategorias = ValuesQuerySetToDict(subcategorias) 

	subcategorias = simplejson.dumps(subcategorias)

	return HttpResponse(subcategorias, content_type="application/json")


@csrf_exempt
def uploadphoto(request):


		caption = request.FILES['file']

		#Guarda foto

		Photo(photo=caption).save()

		id_photo = Photo.objects.all().values('id').order_by('-id')[0]['id']

		caption = '/home/estokeate/'+str(Photo.objects.get(id=id_photo).photo)

		data_json =str(Photo.objects.get(id=id_photo).photo)

		fd_img = open(caption, 'r')

		img = Image.open(fd_img)

		width, height = img.size

		photo = Photo.objects.filter(id=id_photo).values('id','photo')

		# Ruta para la galeria

		if caption.find(".jpg") !=-1:
			formato = '.jpg'

		if caption.find(".png") !=-1:
			formato = '.png'

		if caption.find(".gif") !=-1:
			formato = '.gif'
			
		caption_galeria = caption.split(formato)[0]+'_thumbail.jpg'

		# Guarda galery

		fd_img = open(caption, 'r')

		img = Image.open(fd_img)

		img = resizeimage.resize_cover(img, [width, width])

		img.save(caption_galeria, img.format)

		fd_img.close()

		# Ruta para el home

		caption_home = caption.split(formato)[0]+'_home.jpg'

		fd_img = open(caption, 'r')

		img = Image.open(fd_img)

		img = resizeimage.resize_cover(img, [250, 250])

		img.save(caption_home, img.format)

		fd_img.close()


		# Ruta para la galeria

		caption_galeria = caption.split(formato)[0]+'_thumbail.jpg'





		# Guarda galery

		fd_img = open(caption, 'r')

		img = Image.open(fd_img)

		if int(height) < 400 :


			data_json = simplejson.dumps('Enano')

			return HttpResponse(data_json, content_type="application/json")



		else:

			img = resizeimage.resize_cover(img, [600, 400])



			img.save(caption_galeria, img.format)

			fd_img.close()

			

			

			photo = ValuesQuerySetToDict(photo)

			photo[0]['photo'] = caption_galeria.split('/home/estokeate/')[1]


			data_json = simplejson.dumps(photo)

			return HttpResponse(data_json, content_type="application/json")


		# else:

		# 	photo =simplejson.dumps('Error')

		# 	return HttpResponse(photo, content_type="application/json")






		

@csrf_exempt
def uploadvideo(request):

		caption = request.FILES['file']

		Video(video=caption).save()

		id_video = Video.objects.all().values('id').order_by('-id')[0]['id']

		videodata = Video.objects.filter(id=id_video).values('id','video')

		videodata = ValuesQuerySetToDict(videodata)

		data_json = simplejson.dumps(videodata)

		return HttpResponse(data_json, content_type="application/json")



@csrf_exempt
def verificalogin(request):

	usuario =''

	categoria = ''

	if request.method == 'POST':

		if request.user.is_authenticated():



			data = simplejson.dumps('Logeado')

			return HttpResponse(data, content_type="application/json")

		else:


			data = simplejson.dumps('No-Logeado')

			return HttpResponse(data, content_type="application/json")



@csrf_exempt
def subirimgprofile(request):

	if request.method == 'POST':

		pf= request.POST['img']

		user = request.user.id

		u=AuthUser.objects.get(id=user)
		u.photo = pf
		u.save()

		id_producto = simplejson.dumps('Bienvenido')


		return HttpResponse(id_producto, content_type="application/json")





@csrf_exempt
def animales(request):

	c=Animal.objects.all().values('id','nombre')

	c = ValuesQuerySetToDict(c)

	data_json = simplejson.dumps(c)

	return HttpResponse(data_json, content_type="application/json")

@csrf_exempt
def servicios(request):

	c=Servicios.objects.all().values('id','nombre')

	c = ValuesQuerySetToDict(c)

	data_json = simplejson.dumps(c)

	return HttpResponse(data_json, content_type="application/json")


@csrf_exempt
def empleos(request):

	c=Empleo.objects.all().values('id','nombre')

	c = ValuesQuerySetToDict(c)

	data_json = simplejson.dumps(c)

	return HttpResponse(data_json, content_type="application/json")

@csrf_exempt
def listcursos(request):

	c=Cursos.objects.all().values('id','nombre')

	c = ValuesQuerySetToDict(c)

	data_json = simplejson.dumps(c)

	return HttpResponse(data_json, content_type="application/json")



@csrf_exempt
def mostrarcategorias(request):

	c=Categoria.objects.all().values('id','nombre','icon','imagen','descripcion')

	for p in range(len(c)):

		s = Subcategoria.objects.filter(categoria_id=c[p]['id']).values('id','nombre')

		s = ValuesQuerySetToDict(s)

		c[p]['subcategoria'] = s

	c = ValuesQuerySetToDict(c)

	data_json = simplejson.dumps(c)

	return HttpResponse(data_json, content_type="application/json")




@csrf_exempt
def loginxfacebook(request):

	usuario =''

	categoria = ''

	if request.method == 'POST':

		if request.user.is_authenticated():


			id_producto = simplejson.dumps('Ya esta logeado')

			return HttpResponse(id_producto, content_type="application/json")
		else:

			id= request.POST['id']

			name = request.POST['name']
		
			user = authenticate(username=id, password=id)

			if user is not None:

				if user.is_active:

					login(request, user)

					id_user = request.user.id

					u = AuthUser.objects.get(id=id_user)

					u.first_name = name

					u.save()

					id_producto = simplejson.dumps('Bienvenido'+'-'+str(id_user))

					return HttpResponse(id_producto, content_type="application/json")

			else:

				User.objects.create_user(id, id, id)

				user = authenticate(username=id, password=id)

				id_producto = simplejson.dumps('nuevo user')

				return HttpResponse(id_producto, content_type="application/json")



@login_required(login_url="/autentificacion/")

def addfavorito(request,id,estado):

	if request.method == 'GET':

		user = request.user.id

		if Favoritoproducto.objects.filter(user_id=user,producto_id=id).count()==0:

			Favoritoproducto(user_id=user,producto_id=id,estado=estado).save()

		else:

			f = Favoritoproducto.objects.get(user_id=user,producto_id=id)
			
			f.estado=estado
			f.save()


		id_producto = simplejson.dumps('nuevo user')

		return HttpResponse(id_producto, content_type="application/json")




# @login_required(login_url="/autentificacion/")

# def editarproducto(request,id):


# 	if request.method == 'GET':

# 		producto = Producto.objects.filter(id=id)

# 		photo = Photoproducto.objects.filter(producto_id=id)

# 		m=None
# 		if mobile(request):
# 			m='m'

# 		if m=='m':

# 			return render(request, 'editarproductomovil.html',{'photo':photo,'producto':producto[0],'host':host})


# 		else:

# 			return render(request, 'editarproducto.html',{'photo':photo,'producto':producto[0],'host':host})

# 	if request.method == 'POST':

# 		categoria = request.POST['categoria']

# 		titulo = request.POST['titulo']

# 		descripcion = request.POST['descripcion']

# 		p = Producto.objects.get(id=id)

# 		p.categoria_id = categoria
# 		p.titulo = titulo
# 		p.descripcion = descripcion
# 		p.save()


# 		return render(request, 'editarproducto.html',{'producto':p,'host':host})



@login_required(login_url="/autentificacion")

@csrf_exempt
def vender(request):

	user = request.user.id

	id_user=None

	usuario= None

	if user:

		id_user= AuthUser.objects.get(id=user).id

		usuario=AuthUser.objects.get(id=user)

	if request.method == 'POST':


		data = json.loads(request.body)['dato']

		titulo = data['titulo']
		precio=data['precio']
		descripcion=data['descripcion']
		categoria=data['categoria']
		subcategoria=data['subcategoria']


		marca=None
		modelo=None
		tipo=None
		anio=None
		kilometraje=None
		color=None
		cilindros=None
		transmision=None
		combustible=None
		condicion=None
		animal=None
		provincia=None
		distrito=None
		auto=None
		animal=None
		metros2=None
		ubicacion=None
		empleo=None
		experiencia=None
		salarioestimado=None
		servicio=None
		detalleservicio=None
		dormitorios=None
		banios=None
		piscina=None
		jardin=None
		amueblado=None
		gimnasio=None
		sauna=None
		jacuzzi=None
		ambientes=None
		curso=None
		antiguedad=None

		for p in data:

			if p =='marca': marca= data['marca']
			if p =='modelo': modelo = data['modelo']
			if p =='tipo': tipo =data['tipo']
			if p =='anio': anio =data['anio']
			if p =='kilometraje': kilometraje =data['kilometraje']
			if p =='color':color=data['color']
			if p =='cilindros':cilindros=data['cilindros']
			if p =='transmision': transmision=data['transmision']
			if p =='combustibles':combustible=data['combustible']
			if p =='condicion':condicion=data['condicion']
			if p =='moneda':moneda=data['moneda']
			if p =='animal':animal=data['animal']
			if p =='transaction':tipo=data['transaction']
			if p =='provincia':provincia=data['provincia']
			if p =='distrito':distrito=data['distrito']
			if p=='telefono': telefono=data['telefono']
			if p=='animal': animal=data['animal']
			if p=='metros2': metros2=data['metros2']
			if p=='ubicacion': ubicacion=data['ubicacion']
			if p=='empleo': empleo=data['empleo']
			if p=='experiencia': experiencia=data['experiencia']
			if p=='salarioestimado': salarioestimado=data['salarioestimado']
			if p=='servicio': servicio=data['servicio']
			if p=='dormitorios': dormitorios=data['dormitorios']
			if p=='banios': banios=data['banios']
			if p=='piscina': piscina=data['piscina']
			if p=='jardin': jardin=data['jardin']
			if p=='amueblado': amueblado=data['amueblado']
			if p=='gimnasio': gimnasio=data['gimnasio']
			if p=='sauna': sauna=data['sauna']
			if p=='jacuzzi': jacuzzi=data['jacuzzi']
			if p=='ambientes': ambientes=data['ambientes']
			if p=='curso': curso=data['curso']
			if p=='antiguedad': antiguedad=data['antiguedad']

		if marca and modelo and tipo:

			auto = Auto.objects.get(marca_id=marca,modelo_id=modelo,tipo_id=tipo).id

		Producto(moneda=moneda,auto_id=auto,anio=anio,kilometraje=kilometraje,color_id=color,cilindros=cilindros,transmision=transmision,combustible=combustible,condicion=condicion,animal=animal,transaction=transaction,provincia_id=provincia,distrito_id=distrito,user_id=id_user,titulo=titulo,categoria_id=categoria,subcategoria_id=subcategoria,descripcion=descripcion,precio=precio,metros2=metros2,ubicacion=ubicacion,empleo_id=empleo,experiencia=experiencia,salarioestimado=salarioestimado,servicio_id=servicio,dormitorios=dormitorios,banios=banios,piscina=piscina,jardin=jardin,amueblado=amueblado,gimnasio=gimnasio,sauna=sauna,jacuzzi=jacuzzi,ambientes=ambientes,curso=curso,antiguedad=antiguedad).save()

		id_producto = Producto.objects.all().values('id').order_by('-id')[0]['id']



		for d in data:


			if d=='image':

				image=data['image']

				Photoproducto(photo_id=image,producto_id=id_producto).save()

			if d=='image_1':
			
				image_1 = data['image_1']

				Photoproducto(photo_id=image_1,producto_id=id_producto).save()

			if d=='image_2':

				image_2 = data['image_2']

				Photoproducto(photo_id=image_2,producto_id=id_producto).save()

			if d =='image_3':

				image_3 = data['image_3']

				Photoproducto(photo_id=image_3,producto_id=id_producto).save()


			if d =='image_4':

				image_4 = data['image_4']

				Photoproducto(photo_id=image_4,producto_id=id_producto).save()


			if d =='image_5':

				image_5 = data['image_5']

				Photoproducto(photo_id=image_5,producto_id=id_producto).save()


			if d =='image_6':

				image_6 = data['image_6']

				Photoproducto(photo_id=image_6,producto_id=id_producto).save()

			if d =='video':

				video = data['video']

				Videoproducto(video_id=video,producto_id=id_producto).save()

		# pro =Producto.objects.get(id=id_producto)

		# pro.photo_id=image

		# pro.save()

		res= {'user':id_user,'producto':id_producto}

		id_producto = simplejson.dumps(res)

		


		return HttpResponse(id_producto, content_type="application/json")



	categoria = Categoria.objects.all().values('id','nombre','icon')

	m=None
	if mobile(request):
		m='m'

	if m=='m':

		return render(request, 'vendermovil.html',{'host':host,'usuario':usuario,'categoria':categoria})

	else:

		return render(request, 'vender.html',{'host':host,'usuario':usuario,'categoria':categoria})


def ingresar(request,producto):

	p=None

	if int(producto) != 5 and Producto.objects.filter(id=producto).count()>0:

		p=Producto.objects.get(id=producto)

	if request.user.is_authenticated():

		return HttpResponseRedirect("/vender")

	else:

		if request.method == 'POST':

			user = request.POST['username']
			
			psw = request.POST['password']

			user = authenticate(username=user, password=psw)

			if user is not None:

				if user.is_active:

					login(request, user)

					m=None
					if mobile(request):
						m='m'

					if p:

						if m=='m':

							return HttpResponseRedirect("/detallechat/"+str(p.user.id)+'/'+str(producto))
						
						else:

							return HttpResponseRedirect("/detallechatpc/"+str(p.user.id)+'/'+str(producto))

					else:

							return HttpResponseRedirect("/")

			else:

				return HttpResponseRedirect("/ingresar")
		
		else:


			m=None
			if mobile(request):
				m='m'

			if m=='m':

				return render(request, 'loginmovil.html',{'host':host,'producto':p})

			else:

				return render(request, 'login.html',{'host':host,'producto':p})


def ingresarone(request):

	p=None

	if request.user.is_authenticated():

		return HttpResponseRedirect("/vender")

	else:

		if request.method == 'POST':

			user = request.POST['username']
			
			psw = request.POST['password']

			user = authenticate(username=user, password=psw)

			if user is not None:

				if user.is_active:

					login(request, user)

					m=None
					if mobile(request):
						m='m'

					if p:

						if m=='m':

							return HttpResponseRedirect("/detallechat/"+str(p.user.id)+'/'+str(producto))
						
						else:

							return HttpResponseRedirect("/detallechatpc/"+str(p.user.id)+'/'+str(producto))

					else:

							return HttpResponseRedirect("/")

			else:

				return HttpResponseRedirect("/ingresar")
		
		else:


			m=None
			if mobile(request):
				m='m'

			if m=='m':

				return render(request, 'loginmovil.html',{'host':host})

			else:

				return render(request, 'login.html',{'host':host})



def categorias(request):

	c = Categoria.objects.all().values('id','nombre','imagen','icon').order_by('-nombre')

	c = ValuesQuerySetToDict(c)

	data_json = simplejson.dumps(c)



	return HttpResponse(data_json, content_type="application/json")
