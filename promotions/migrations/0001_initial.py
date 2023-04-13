# Generated by Django 3.2 on 2023-04-12 23:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Titulo de la promocion')),
                ('description', models.TextField(verbose_name='Descripcion de la promocion')),
                ('image_portada', models.ImageField(upload_to='', verbose_name='Imagen Modal')),
                ('url_video', models.URLField(verbose_name='Youtube URL')),
                ('date_deactivate', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activa')),
            ],
            options={
                'verbose_name': 'Promocion',
                'verbose_name_plural': 'Promociones',
            },
        ),
    ]
