from django.db import models
from django.utils import timezone


# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'region'


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region', default=1)

    class Meta:
        db_table = 'comuna'


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='id_comuna', default=1)

    class Meta:
        db_table = 'sucursal'


class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    class Meta:
        db_table = 'marca'


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria', default=1)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, db_column='id_sucursal', default=1)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, db_column='id_marca', default=1)
    stock = models.IntegerField()
    lanzamiento_reciente = models.BooleanField()
    descripcion = models.CharField(max_length=255)
    porcentaje_descuento = models.IntegerField()

    class Meta:
        db_table = 'producto'


class HistorialPrecio(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto', default=1)
    precio_final = models.IntegerField()
    fecha = models.DateField()

    class Meta:
        db_table = 'historial_precio'


class Trabajador(models.Model):
    run = models.CharField(max_length=10, primary_key=True)
    nombres = models.CharField(max_length=100)
    ape_paterno = models.CharField(max_length=100)
    ape_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.BigIntegerField()
    correo = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, db_column='id_sucursal', default=1)

    class Meta:
        db_table = 'trabajador'


class Cliente(models.Model):
    run_cliente = models.CharField(max_length=10, primary_key=True)
    nombres = models.CharField(max_length=100)
    ape_paterno = models.CharField(max_length=100)
    ape_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.BigIntegerField()
    correo = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='id_comuna', default=1)

    class Meta:
        db_table = 'cliente'

    
class Chat(models.Model):
    emisor = models.CharField(max_length=255, default='erw.gonzalez@duocuc.cl')
    receptor = models.CharField(max_length=255,default='erw.gonzalez@duocuc.cl')
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'chat'