# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_delete_financeiro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=255)),
                ('entrada', models.CharField(max_length=255)),
                ('saida', models.CharField(max_length=255)),
                ('total', models.CharField(max_length=255)),
            ],
        ),
    ]
