# Generated by Django 5.0.6 on 2024-05-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
