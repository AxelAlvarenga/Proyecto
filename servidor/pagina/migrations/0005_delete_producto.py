# Generated by Django 3.2.8 on 2021-11-11 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_rename_productos_producto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
