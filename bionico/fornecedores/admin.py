from django.contrib import admin
from .models import EnderecoFornecedor, Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    model = EnderecoFornecedor
    list_display = (
        'codigo',
        'nome_fant',
        'razao',
        'cnpj',
        'ins_est',
        'contato',
        'nrTelCelular',
        'nrTelFixo',
        'endereco',
        'tipo',
    )

    list_filter = ('tipo',)
    search_fields = ('nome_fant',)


@admin.register(EnderecoFornecedor)
class EnderecoFornecedorAdmin(admin.ModelAdmin):
    model = EnderecoFornecedor
    list_display = (
        'rua',
        'numero',
        'bairro',
        'ponto_rf',
        'cep',
        'cidade',
        'uf',
        'pais',
    )

    list_filter = ('bairro', 'cidade', 'uf',)
    search_fields = ('rua',)
