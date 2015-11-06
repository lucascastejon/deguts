# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
        ('cliente', '0003_clientes'),
        ('core', '0002_delete_vendas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('descricao', models.CharField(default=b'', max_length=255)),
                ('tipo', models.CharField(default=b'EN', max_length=7, choices=[(b'EN', b'Entrada'), (b'SA', b'Sa\xc3\xadda')])),
                ('entrada', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('saida', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('total', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(to='cliente.Clientes')),
                ('produto', models.ForeignKey(to='produto.Produtos')),
            ],
        ),
    ]
