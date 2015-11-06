# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
