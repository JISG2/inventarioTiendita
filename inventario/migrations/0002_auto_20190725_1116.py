# Generated by Django 2.1.5 on 2019-07-25 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aminoacidosmodel',
            name='urlImagen',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glutaminasmodel',
            name='urlImagen',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proteinasmodel',
            name='urlImagen',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aminoacidosmodel',
            name='cantidadServicios',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='proteinasmodel',
            name='servicios',
            field=models.IntegerField(),
        ),
    ]
