# Generated by Django 4.1.2 on 2022-11-21 21:57

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_familiaquestionario_motivolugarviolento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiaquestionario',
            name='preenchido',
            field=models.BooleanField(default=False, verbose_name='Registro preenchido/válido'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='criancasFrequentamEscola',
            field=models.CharField(choices=[('NAOHA', 'Não há crianças'), ('SIM', 'Sim'), ('NAO', 'Não')], max_length=6, null=True, verbose_name='Crianças na Escola'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='frequentaReligiao',
            field=models.CharField(choices=[('NENHUM', 'Nenhuma'), ('CATOLI', 'Católica'), ('EVANGE', 'Evangélica'), ('TJEOVA', 'Testemunhas Jeová'), ('ESPIRI', 'Espírita'), ('OUTROS', 'Outras')], max_length=6, null=True, verbose_name='Frequentam Alguma Religião'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='maiorGrauEscolaridade',
            field=models.CharField(choices=[('FUN_IN', 'Fundamental Incompleto'), ('FUN_CP', 'Fundamental Completo'), ('MED_IN', 'Médio Incompleto'), ('MED_CP', 'Médio Completo'), ('SUP_IN', 'Superior Incompleto'), ('SUP_CP', 'Superior Completo')], max_length=6, null=True, verbose_name='Maior Grau Escolaridade'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='moradiaLugarViolento',
            field=models.BooleanField(default=False, null=True, verbose_name='Lugar Violento'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='motivoLugarViolento',
            field=models.CharField(choices=[('ASSALT', 'Assaltos'), ('DROGAS', 'Tráfico/Uso Drogas'), ('PROSTI', 'Prostituição'), ('OUTROS', 'Outros')], max_length=6, null=True, verbose_name='Lugar Violência'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='pessoasMenores',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Pessoas Menores'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='pessoasNaCasa',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='Pessoas na Casa'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='qtdeDoentes',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Pessoas Doentes'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='qtdeTrabalham',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Pessoas Trabalham'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='qtdeTrabalhoAutonomo',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Trabalho Autônomo'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='qtdeTrabalhoFormal',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Trabalho Formal'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='qtdeTrabalhoInformal',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Trabalho Informal'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='recebeAuxilioGoverno',
            field=models.BooleanField(default=False, null=True, verbose_name='Recebe Auxílio Governo'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='rendaBrutaFamiliar',
            field=models.CharField(choices=[('MENOS1', 'Menos Salário Mínimo'), ('EXATO1', '1 Salário Mínimo'), ('EXATO2', '2 Salários Mínimos'), ('EXATO3', '3 Salários Mínimos'), ('ACIMA3', 'Acima 3 Salários Mínimos')], max_length=6, null=True, verbose_name='Renda Bruta Familiar'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='tipoMoradia',
            field=models.CharField(choices=[('ALUGAD', 'Alugada'), ('CEDIDA', 'Cedida'), ('FINANC', 'Própria Financiada'), ('QUITAD', 'Própria Quitada')], default='ALUGAD', max_length=6, null=True, verbose_name='Tipo Moradia'),
        ),
        migrations.AlterField(
            model_name='familiaquestionario',
            name='valorMoradia',
            field=models.DecimalField(decimal_places=2, help_text='Informe o valor mensal de financiamento ou aluguel', max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Financiamento/Aluguel'),
        ),
    ]