# Generated by Django 3.2.8 on 2022-01-25 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0013_alter_producto_categoria_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_productos',
            field=models.IntegerField(),
        ),
    ]