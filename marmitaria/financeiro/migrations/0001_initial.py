# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=255)),
                ('entrada', models.CharField(max_length=255)),
                ('saida', models.CharField(max_length=255)),
                ('total', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
