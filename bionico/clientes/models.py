from django.db import models


class Endereco(models.Model):

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
    uf = models.CharField(max_length=2, choices=UF_CHOICES)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua


class Cliente(models.Model):

    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    dtNasc = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    nrTelFixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome



