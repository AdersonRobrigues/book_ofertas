# Generated by Django 4.0.2 on 2022-02-01 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_bookvenda_bookvendamerc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookvenda',
            old_name='Operador1',
            new_name='Operador3',
        ),
        migrations.RenameField(
            model_name='bookvenda',
            old_name='Operador2',
            new_name='Operador4',
        ),
    ]
