from django.db import models

# tabela de clientes
class Clientes(models.Model):
    nome = models.CharField(max_length=255, default='')
    telefone = models.CharField(max_length=255, default='')
    endereco = models.CharField(max_length=255, default='')
    criado = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nome
