# Generated by Django 4.0.2 on 2022-02-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_remove_bookcompra_operador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcompra',
            name='Operador',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookvenda',
            name='Operador',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
