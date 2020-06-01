from django.db import models


class TimeStampedModel(models.Model):
    """
    auto insere a data no momento da criação
    do registro / altera a data somente quando
    o registro é alterado

    """
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        """ Poderá ser usado como herança
        em outras Classes """
        abstract = True