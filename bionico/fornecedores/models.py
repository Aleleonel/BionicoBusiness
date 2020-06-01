from django.db import models


class EnderecoFornecedor(models.Model):

    UF_CHOICES = (
        ('AC', u'Acre'),
        ('AL', u'Alagoas'),
        ('AP', u'Amapá'),
        ('AM', u'Amazonas'),
        ('BA', u'Bahia'),
        ('CE', u'Ceará'),
        ('DF', u'Distrito Federal'),
        ('ES', u'Espírito Santo'),
        ('GO', u'Goiás'),
        ('MA', u'Maranhão'),
        ('MT', u'Mato Grosso'),
        ('MS', u'Mato Grosso do Sul'),
        ('MG', u'Minas Gerais'),
        ('PA', u'Pará'),
        ('PB', u'Paraíba'),
        ('PR', u'Paraná'),
        ('PE', u'Pernambuco'),
        ('PI', u'Piauí'),
        ('RJ', u'Rio de Janeiro'),
        ('RN', u'Rio Grande do Norte'),
        ('RS', u'Rio Grande do Sul'),
        ('RO', u'Rondônia'),
        ('RR', u'Roraima'),
        ('RR', u'Roraima'),
        ('SC', u'Santa Cataria'),
        ('SP', u'São Paulo'),
        ('SE', u'Sergipe'),
        ('TO', u'Tocantins'),

    )

    rua = models.CharField(max_length=60)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=30)
    ponto_rf = models.CharField(max_length=30, null=True, blank=True, verbose_name='ponto de referência')
    cidade = models.CharField(max_length=60)
    cep = models.CharField(max_length=8, null=False, blank=False)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua


class Fornecedor(models.Model):

    PRODUTOS_CHOICES = (
        ('A', u'Alimento'),
        ('B', u'Bebida'),
        ('L', u'Limpeza'),
        ('U', u'Utencilhos'),
    )

    codigo = models.IntegerField(unique=True)
    cnpj = models.CharField(max_length=14, null=False, blank=False, unique=True)
    ins_est = models.CharField(max_length=14, null=False, blank=False, verbose_name='inscrição estadual', unique=True)
    nome_fant = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome fantasia')
    razao = models.CharField(max_length=60, null=False, blank=False, verbose_name='razão social')
    contato = models.CharField(max_length=10)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    nrTelFixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    endereco = models.OneToOneField(EnderecoFornecedor, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=1, choices=PRODUTOS_CHOICES)

    def __str__(self):
        return self.nome_fant