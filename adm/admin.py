from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'lanzamiento_reciente', 'descripcion', 'porcentaje_descuento']
    readonly_fields = ['nombre', 'stock', 'descripcion']
    exclude = ['id_categoria', 'id_sucursal', 'id_marca']

admin.site.register(Producto, ProductoAdmin)