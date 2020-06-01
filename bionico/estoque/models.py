from django.contrib.auth.models import User
from django.db import models
from bionico.core.models import TimeStampedModel
from bionico.produto.models import Produto


MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    """
        Definido em minha app core a class TimeStampedModel
        tem um campo chamando created, onde defino data de criação
        do arquivo e data de alateração do aquirvo sendo a primeira
        gerada automaticamente. Ao defini-la como object-Abstract
        no permitira utiliza-la em qualquer parte do projeto
    """
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.pk)


class EstoqueItens(models.Model):
    """
        Tabela intermediária para controle das entradas e
        saidas dos produtos
    """
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{}- {} - {}'.format(self.pk, self.estoque.pk, self.produto)