# Generated by Django 3.2.8 on 2022-01-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='compra_proveedor',
            fields=[
                ('codigo_productos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_productos', models.CharField(max_length=50)),
                ('preciocompra_productos', models.IntegerField()),
                ('categoria_productos', models.IntegerField()),
                ('cantidad_productos', models.IntegerField()),
            ],
        ),
    ]