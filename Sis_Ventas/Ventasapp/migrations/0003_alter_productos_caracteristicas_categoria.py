# Generated by Django 5.1.3 on 2024-11-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventasapp', '0002_alter_productos_caracteristicas_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='caracteristicas_categoria',
            field=models.CharField(choices=[('Varios', 'Varios'), ('Comidas', 'Comidas'), ('Ropa', 'Ropa'), ('Bebidas', 'Bebidas'), ('Limpieza', 'Limpieza')], max_length=100),
        ),
    ]
