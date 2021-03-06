# Generated by Django 3.0.6 on 2020-05-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnderecoFornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=60)),
                ('numero', models.CharField(max_length=5)),
                ('bairro', models.CharField(max_length=30)),
                ('ponto_rf', models.CharField(blank=True, max_length=30, null=True, verbose_name='ponto de referência')),
                ('cidade', models.CharField(max_length=60)),
                ('cep', models.CharField(max_length=8)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RR', 'Roraima'), ('SC', 'Santa Cataria'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('ins_est', models.CharField(max_length=14, unique=True, verbose_name='inscrição estadual')),
                ('nome_fant', models.CharField(max_length=60, verbose_name='nome fantasia')),
                ('razao', models.CharField(max_length=60, verbose_name='razão social')),
                ('contato', models.CharField(max_length=10)),
                ('nrTelCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('nrTelFixo', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone fixo')),
                ('tipo', models.CharField(choices=[('A', 'Alimento'), ('B', 'Bebida'), ('L', 'Limpeza'), ('U', 'Utencilhos')], max_length=1)),
                ('endereco', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fornecedores.EnderecoFornecedor')),
            ],
        ),
    ]
