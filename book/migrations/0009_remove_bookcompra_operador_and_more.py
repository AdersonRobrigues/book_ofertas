# Generated by Django 4.0.2 on 2022-02-04 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_bookcompra_operador1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcompra',
            name='Operador',
        ),
        migrations.RemoveField(
            model_name='bookvenda',
            name='Operador1',
        ),
        migrations.RemoveField(
            model_name='bookvenda',
            name='Operador2',
        ),
    ]
