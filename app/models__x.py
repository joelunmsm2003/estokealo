BASE_DIR /home/estokeate
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Animal(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    photo = models.CharField(max_length=11000, blank=True, null=True)
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Auto(models.Model):
    marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='marca', blank=True, null=True)
    modelo = models.ForeignKey('Modelo', models.DO_NOTHING, db_column='modelo', blank=True, null=True)
    tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='tipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto'


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Chat(models.Model):
    user = models.IntegerField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'


class Color(models.Model):
    nombre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'


class Distrito(models.Model):
    nombre = models.IntegerField(blank=True, null=True)
    provincia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distrito'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Favoritoproducto(models.Model):
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto', blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favoritoproducto'


class Marca(models.Model):
    nombre = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'


class Modelo(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelo'


class Notificacion(models.Model):
    payload = models.CharField(max_length=10000, blank=True, null=True)
    auth = models.CharField(max_length=10000, blank=True, null=True)
    endpoint = models.CharField(max_length=10000, blank=True, null=True)
    p256dh = models.CharField(max_length=10000, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'


class Photo(models.Model):
    photo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class Photoproducto(models.Model):
    photo = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photoproducto'


class Producto(models.Model):
    user = models.IntegerField(blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=1000, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    subcategoria = models.IntegerField(blank=True, null=True)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, db_column='auto', blank=True, null=True)
    anio = models.CharField(max_length=100, blank=True, null=True)
    kilometraje = models.CharField(max_length=1000, blank=True, null=True)
    color = models.ForeignKey(Color, models.DO_NOTHING, db_column='color', blank=True, null=True)
    cilindros = models.CharField(max_length=1000, blank=True, null=True)
    transmision = models.CharField(max_length=100, blank=True, null=True)
    combustible = models.CharField(max_length=1000, blank=True, null=True)
    condicion = models.CharField(max_length=1000, blank=True, null=True)
    moneda = models.CharField(max_length=1000, blank=True, null=True)
    transaction = models.CharField(max_length=1000, blank=True, null=True)
    distrito = models.ForeignKey(Distrito, models.DO_NOTHING, db_column='distrito', blank=True, null=True)
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    animal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Provincia(models.Model):
    name = models.CharField(max_length=110, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Subcategoria(models.Model):
    categoria = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategoria'


class Tipo(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'


class Video(models.Model):
    video = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video'


class Videoproducto(models.Model):
    video = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videoproducto'
