# Generated by Django 5.0 on 2024-04-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_direccion_alter_usuario_options_alter_usuario_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='casa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='municipio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='provincia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
