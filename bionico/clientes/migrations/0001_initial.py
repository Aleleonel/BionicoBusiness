# Generated by Django 3.0.6 on 2020-05-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('dtNasc', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('estado_civil', models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=1, verbose_name='Estado civil')),
                ('nrTelCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('nrTelFixo', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone fixo')),
            ],
        ),
    ]