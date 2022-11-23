# Generated by Django 4.1.2 on 2022-11-21 21:30

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_unidadeorganizacao_metaqtdecestas'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaQuestionario',
            fields=[
                ('familia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pages.familiaatendida')),
                ('tipoMoradia', models.CharField(choices=[('ALUGAD', 'Alugada'), ('CEDIDA', 'Cedida'), ('FINANC', 'Própria Financiada'), ('QUITAD', 'Própria Quitada')], max_length=6, null=True, verbose_name='Tipo Moradia')),
                ('valorMoradia', models.DecimalField(decimal_places=2, help_text='Informe o valor mensal de financiamento ou aluguel', max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Financiamento/Aluguel')),
                ('moradiaLugarViolento', models.BooleanField(default=False, verbose_name='Lugar Violento')),
                ('motivoLugarViolento', models.CharField(choices=[('ASSALT', 'Assaltos'), ('DROGAS', 'Tráfico/Uso Drogas'), ('PROSTI', 'Prostituição'), ('OUTROS', 'Outros')], max_length=6, null=True, verbose_name='Lugar Violência')),
                ('pessoasNaCasa', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='Pessoas na Casa')),
                ('pessoasMenores', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Pessoas Menores')),
                ('criancasFrequentamEscola', models.CharField(choices=[('NAOHA', 'Não há crianças'), ('SIM', 'Sim'), ('NAO', 'Não')], max_length=6, verbose_name='Crianças na Escola')),
                ('qtdeDoentes', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Pessoas Doentes')),
                ('qtdeTrabalham', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Pessoas Trabalham')),
                ('qtdeTrabalhoFormal', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Trabalho Formal')),
                ('qtdeTrabalhoAutonomo', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Trabalho Autônomo')),
                ('qtdeTrabalhoInformal', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Quantas Trabalho Informal')),
                ('rendaBrutaFamiliar', models.CharField(choices=[('MENOS1', 'Menos Salário Mínimo'), ('EXATO1', '1 Salário Mínimo'), ('EXATO2', '2 Salários Mínimos'), ('EXATO3', '3 Salários Mínimos'), ('ACIMA3', 'Acima 3 Salários Mínimos')], max_length=6, verbose_name='Renda Bruta Familiar')),
                ('recebeAuxilioGoverno', models.BooleanField(default=False, verbose_name='Recebe Auxílio Governo')),
                ('maiorGrauEscolaridade', models.CharField(choices=[('FUN_IN', 'Fundamental Incompleto'), ('FUN_CP', 'Fundamental Completo'), ('MED_IN', 'Médio Incompleto'), ('MED_CP', 'Médio Completo'), ('SUP_IN', 'Superior Incompleto'), ('SUP_CP', 'Superior Completo')], max_length=6, verbose_name='Maior Grau Escolaridade')),
                ('frequentaReligiao', models.CharField(choices=[('NENHUM', 'Nenhuma'), ('CATOLI', 'Católica'), ('EVANGE', 'Evangélica'), ('TJEOVA', 'Testemunhas Jeová'), ('ESPIRI', 'Espírita'), ('OUTROS', 'Outras')], max_length=6, verbose_name='Frequentam Alguma Religião')),
            ],
        ),
    ]
