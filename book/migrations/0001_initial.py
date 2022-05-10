# Generated by Django 4.0.1 on 2022-01-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvOfertasMrt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Operador1', models.BooleanField(default=False)),
                ('tp_energia', models.CharField(choices=[('CONV', 'conv'), ('I5', 'i5'), ('I1', 'i1'), ('I0', 'i0'), ('CQ5', 'cq5')], max_length=5)),
                ('prod_ini', models.CharField(choices=[(1, 'JAN'), (2, 'FEV'), (3, 'MAR'), (4, 'ABR'), (5, 'MAI'), (6, 'JUN'), (7, 'JUL'), (8, 'AGO'), (9, 'SET'), (10, 'OUT'), (11, 'NOV'), (12, 'DEZ')], max_length=5)),
                ('prod_fim', models.CharField(choices=[(1, 'JAN'), (2, 'FEV'), (3, 'MAR'), (4, 'ABR'), (5, 'MAI'), (6, 'JUN'), (7, 'JUL'), (8, 'AGO'), (9, 'SET'), (10, 'OUT'), (11, 'NOV'), (12, 'DEZ')], max_length=5)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=6)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('submer', models.CharField(choices=[('SE', 'se'), ('SU', 'su'), ('NE', 'ne'), ('NO', 'no')], max_length=2)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
