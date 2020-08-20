# Generated by Django 3.0.4 on 2020-07-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_auto_20200716_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='cp',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registro',
            name='opcion',
            field=models.CharField(choices=[('Curso Valuacion de bienes distintos a la tierra', 'Curso Valuación de bienes distintos a la tierra $1,595.00 MXN'), ('Curso Valuacion de inmuebles rusticos con presion urbana', 'Curso Valuación de inmuebles rústicos con presión urbana $1,595.00 MXN'), ('Curso Valuacion economica de impacto ambiental por el Metodo de valoracion contingente', 'Curso Valuación económica de impacto ambiental por el Método de Valoración Contingente $1,595.00 MXN'), ('Simposio y curso', 'Simposio y curso $2,900.00 MXN')], max_length=100, verbose_name='Paquete seleccionado'),
        ),
    ]