# Generated by Django 4.0.3 on 2022-03-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_bookcompramerc_agente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcompra',
            name='Operador',
            field=models.CharField(choices=[('Raul', 'RAUL'), ('Isabella', 'ISABELLA'), ('Eduardo', 'EDUARDO'), ('Aderson', 'ADERSON')], max_length=50),
        ),
    ]
