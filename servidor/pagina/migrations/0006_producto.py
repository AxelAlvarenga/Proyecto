# Generated by Django 3.2.8 on 2021-11-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codigo_productos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_productos', models.CharField(max_length=50)),
                ('preciocompra_productos', models.IntegerField()),
                ('precioventa_productos', models.IntegerField()),
                ('categoria_productos', models.CharField(max_length=50)),
                ('cantidad_productos', models.IntegerField()),
            ],
        ),
    ]