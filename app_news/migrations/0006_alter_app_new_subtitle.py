# Generated by Django 3.2 on 2023-04-23 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_alter_app_new_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_new',
            name='subtitle',
            field=models.TextField(max_length=100, verbose_name='Resumen'),
        ),
    ]