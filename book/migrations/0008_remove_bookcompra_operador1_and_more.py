# Generated by Django 4.0.2 on 2022-02-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_rename_operador3_bookvenda_operador1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcompra',
            name='Operador1',
        ),
        migrations.RemoveField(
            model_name='bookcompra',
            name='Operador2',
        ),
        migrations.AddField(
            model_name='bookcompra',
            name='Operador',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
