# Generated by Django 3.0.5 on 2020-04-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0007_auto_20200425_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='comentarios',
            field=models.TextField(),
        ),
    ]