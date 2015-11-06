# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='cliente',
            field=models.ForeignKey(to='cliente.Clientes', null=True),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='descricao',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='entrada',
            field=models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='produto',
            field=models.ForeignKey(to='produto.Produtos', null=True),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='saida',
            field=models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='tipo',
            field=models.CharField(default=b'EN', max_length=7, null=True, choices=[(b'EN', b'Entrada'), (b'SA', b'Sa\xc3\xadda')]),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='total',
            field=models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2),
        ),
    ]
