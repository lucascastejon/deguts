from django.db import models

# Tabela do financeiro
class Financeiro(models.Model):
    descricao = models.CharField(max_length=255)
    entrada = models.CharField(max_length=255)
    saida = models.CharField(max_length=255)
    total = models.CharField(max_length=255)

    def __unicode__(self):
        return self.descricao
