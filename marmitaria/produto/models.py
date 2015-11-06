from django.db import models

# Tabela de produtos
class Produtos(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    criado = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.descricao
