from django.db import models
from.choices import CATEGORIAS
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator ,MinLengthValidator
# Create your models here.

class Clientes(models.Model):
    cedula=models.CharField(primary_key=True,max_length=10,unique=True,validators=[MinLengthValidator(10)])
    nombre=models.CharField(max_length=50,blank=True,verbose_name='Nombre del Clientes')
    apellidos=models.CharField(max_length=50,blank=False)
    telefono=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    direccion=models.TimeField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return f"{self.nombre} ''{self.apellido}"
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table='Clientes'
    
class Productos(models.Model):
        codigo = models.CharField(primary_key=True,max_length=10,unique=True)
        nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre del Product')
        marca=models.CharField(max_length=50,unique=True)   
        caracteristicas_categoria=models.CharField(max_length=100,choices=CATEGORIAS)
        precio=models.DecimalField(max_digits=10, decimal_places=2,help_text='ingresa valores con decimales',verbose_name='Precio')
        cantidad_stock=models.IntegerField(verbose_name='Cantidad de stock')
        fecha_ingreso=models.DateTimeField(auto_now_add=True)
        fecha_vencimiento=models.DateField()
        fecha_elaboracion=models.DateField()

        def __str__(self):
            return f"{self.nombre} ''{self.marca}"
        
        class Meta: 
            verbose_name = 'Producto'   
            verbose_name_plural = 'Productos'
            db_table='Productos'    