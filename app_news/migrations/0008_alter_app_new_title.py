# Generated by Django 3.2 on 2023-04-23 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0007_alter_app_new_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_new',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titular'),
        ),
    ]
