# Generated by Django 4.0.3 on 2022-05-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0024_bookcompra_tp_preco_bookcompramerc_tp_preco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcompramerc',
            name='agente',
        ),
        migrations.RemoveField(
            model_name='bookvendamerc',
            name='agente',
        ),
        migrations.AddField(
            model_name='bookcompramerc',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Checked'),
        ),
        migrations.AddField(
            model_name='bookvendamerc',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Checked'),
        ),
        migrations.AlterField(
            model_name='bookcompramerc',
            name='tp_preco',
            field=models.CharField(blank=True, choices=[('Fixo', 'FIXO'), ('Pld', 'PLD')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='bookvenda',
            name='tp_preco',
            field=models.CharField(blank=True, choices=[('Fixo', 'FIXO'), ('Pld', 'PLD')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='bookvendamerc',
            name='tp_preco',
            field=models.CharField(blank=True, choices=[('Fixo', 'FIXO'), ('Pld', 'PLD')], max_length=5, null=True),
        ),
    ]
