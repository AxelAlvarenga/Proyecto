# Generated by Django 3.2.8 on 2021-11-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='cantidad_producto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='codigo_producto',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productos',
            name='preciocompra_producto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precioventa_producto',
            field=models.IntegerField(),
        ),
    ]