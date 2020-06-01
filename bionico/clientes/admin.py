from django.contrib import admin
from .models import Cliente, Endereco


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = (
        'nome',
        'cpf',
        'dtNasc',
        'sexo',
        'estado_civil',
        'nrTelCelular',
        'nrTelFixo',
        'endereco',
    )

    list_filter = ('sexo', 'estado_civil',)
    search_fields = ('nome',)


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    model = Endereco
    list_display = (
        'rua',
        'numero',
        'bairro',
        'ponto_rf',
        'cidade',
        'uf',
        'pais',
    )

    list_filter = ('uf',)
    search_fields = ('rua',)


