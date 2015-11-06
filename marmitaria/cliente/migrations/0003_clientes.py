# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_delete_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=255)),
                ('telefone', models.CharField(default=b'', max_length=255)),
                ('endereco', models.CharField(default=b'', max_length=255)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
