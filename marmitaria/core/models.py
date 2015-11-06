# coding: utf-8
from django.db import models
from marmitaria.cliente.models import Clientes
from marmitaria.produto.models import Produtos
from marmitaria.financeiro.models import Financeiro

TYPES = (
    ('EN', 'Entrada'),
    ('SA', 'Saída'),
)
# Tabelas de vendas
class Vendas(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=255, default='', null=True)
    cliente = models.ForeignKey(Clientes, null=True)
    produto = models.ForeignKey(Produtos, null=True)
    tipo = models.CharField(max_length=7, choices=TYPES, default='EN', null=True)
    entrada = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, null=True)
    saida = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, null=True)
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, null=True)

    criado = models.DateTimeField(auto_now_add=True)

    def somartotal(self):
        return str(Vendas.objects.)
    def __unicode__(self):
        return self.descricao
