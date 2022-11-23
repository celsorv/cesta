from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from decimal import Decimal

class UnidadeOrganizacao(models.Model):
    
    nome = models.CharField(
        max_length=50,
    )
    ativo = models.BooleanField(
        default=True,
    )
    diasEsperaAgendadas = models.PositiveSmallIntegerField(
        db_column='dias_espera_agendadas', 
        default=1, 
        null=False, 
        verbose_name='Doação Agendada - Dias de Espera',
    )

    def __str__(self):
        return self.nome

class FamiliaAtendida(models.Model):

    unidadeOrganizacao = models.ForeignKey(
        UnidadeOrganizacao, 
        on_delete=models.PROTECT, 
        db_column='unidade_org_id', 
        default=1,
        verbose_name='Unidade Organização',
    )
    nome = models.CharField(
        max_length=50,
    )
    ativo = models.BooleanField(
        default=True,
        verbose_name='Família Ativa?'
    )
    qtdeCestas = models.PositiveSmallIntegerField(
        db_column='qtde_cestas',
        default=1,
        null=False,
        verbose_name="Quantidade Cestas",
        help_text='Informe a quantidade de cestas necessárias',
    )
    logradouro = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='',
        verbose_name='Logradouro',
        help_text='Informe o logradouro e número do endereço',
    )
    complemento = models.CharField(
        max_length=30,
        default='',
        blank=True,
        null=True,
        verbose_name='Complemento',
        help_text='Informe o complemento do endereço',
    )
    bairro = models.CharField(
        max_length=30,
        default='',
        blank=True,
        null=True,
        verbose_name='Bairro',
        help_text='Informe o bairro do endereço',
    )
    telefone = models.CharField(
        max_length=50,
        default='',
        blank=True,
        null=True,
        verbose_name='Telefone',
        help_text='Informe os telefones de contato',
    )
    observacoes = models.CharField(
        max_length=255,
        default='',
        blank=True,
        null=True,
        verbose_name='Observações',
        help_text='Informe observações importantes',
    )
    
    def __str__(self):
        return self.nome

class FamiliaQuestionario(models.Model):

    TIPO_MORADIA = (
        ('QUITAD', 'Própria Quitada'),
        ('FINANC', 'Própria Financiada'),
        ('ALUGAD', 'Alugada'),
        ('CEDIDA', 'Cedida'),
    )

    RENDA_BRUTA_FAMILIAR = (
        ('MENOS1', 'Até um salário mínimo'),
        ('EXATO1', 'Um salário mínimo'),
        ('EXATO2', 'Dois salários mínimos'),
        ('EXATO3', 'Três salários mínimos'),
        ('ACIMA3', 'Acima de três salários mínimos'),
    )

    GRAU_ESCOLARIDADE = (
        ('FUN_IN', 'Fundamental Incompleto'),
        ('FUN_CP', 'Fundamental Completo'),
        ('MED_IN', 'Médio Incompleto'),
        ('MED_CP', 'Médio Completo'),
        ('SUP_IN', 'Superior Incompleto'),
        ('SUP_CP', 'Superior Completo'),
    )

    RELIGIAO = (
        ('NENHUM', 'Nenhuma'),
        ('CATOLI', 'Católica'),
        ('EVANGE', 'Evangélica'),
        ('TJEOVA', 'Testemunhas Jeová'),
        ('ESPIRI', 'Espírita'),
        ('OUTROS', 'Outras'),
    )

    TIPO_VIOLENCIA = (
        ('ASSALT', 'Assaltos'),
        ('DROGAS', 'Tráfico/Uso Drogas'),
        ('PROSTI', 'Prostituição'),
        ('OUTROS', 'Outros'),
    )

    CRIANCAS_NA_ESCOLA = (
        ('NAOHA', 'Não há crianças'),
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    )

    familia = models.OneToOneField(
        FamiliaAtendida,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    tipoMoradia = models.CharField(
        max_length=6,
        choices=TIPO_MORADIA,
        verbose_name='1. Qual o tipo de moradia onde a família reside?',
        blank=False,
        null=True,
    )

    valorMoradia = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal(0.00))], 
        verbose_name='Em caso de financiamento ou aluguel informe o valor pago mensalmente:',
        null=True,
    )

    moradiaLugarViolento = models.BooleanField(
        blank=False,
        null=True,
    )

    motivoLugarViolento = models.CharField(
        max_length=6,
        choices=TIPO_VIOLENCIA,
        verbose_name='Lugar Violência',
        blank=False,
        null=True,
    )

    pessoasNaCasa = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)], 
        verbose_name='3. Quantas pessoas vivem na casa?',
        null=True,
    )

    pessoasMenores = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(20)],
        verbose_name='4. Das pessoas que residem na casa, quantas são menores de 18 anos?',
        null=True,
    )

    criancasFrequentamEscola = models.CharField(
        max_length=6,
        choices=CRIANCAS_NA_ESCOLA,
        blank=False,
        null=True,
    )

    temPessoasDoentes = models.BooleanField(
        blank=False,
        null=True,
    )

    qtdeDoentes = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(20)],
        verbose_name='6.1. Se sim, quantas pessoas doentes ou com necessidades especiais?',
        null=True,
    )

    qtdeTrabalham = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(20)],
        verbose_name='7. Das pessoas que residem na casa, quantas trabalham e contribuem com a renda familiar?',
        null=True,
    )

    qtdeTrabalhoFormal = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(20)],
        verbose_name='8. Das pessoas que trabalham, quantas trabalham em empregos formais com carteira assinada?',
        null=True,
    )

    qtdeTrabalhoAutonomo = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(20)],
        verbose_name='9. Das pessoas que trabalham, quantas são autônomas?',
        null=True,
    )

    qtdeTrabalhoInformal = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(20)],
        verbose_name='10. Das pessoas que trabalham, quantas trabalham informalmente sem vínculo empregatício ou fazendo bicos?',
        null=True,
    )

    rendaBrutaFamiliar = models.CharField(
        max_length=6,
        choices=RENDA_BRUTA_FAMILIAR,
        blank=False,
        null=True,
    )

    recebeAuxilioGoverno = models.BooleanField(
        blank=False,
        null=True,
    )

    maiorGrauEscolaridade = models.CharField(
        max_length=6,
        choices=GRAU_ESCOLARIDADE,
        blank=False,
        null=True,
    )

    frequentaReligiao = models.CharField(
        max_length=6,
        choices=RELIGIAO,
        blank=False,
        null=True,
    )

    respondido = models.BooleanField(
        default=False,
        null=False,
    )

    @receiver(post_save, sender=FamiliaAtendida)
    def cria_questionario_familia(sender, instance, created, **kwargs):
        if created:
            FamiliaQuestionario.objects.get_or_create(pk=instance.pk)

    def __str__(self):
        return self.familia


class GrupoProduto(models.Model):

    UNIDADE_CHOICES = (
        ('KG', 'Quilograma (kg)'),
        ('GR', 'Grama (g)'),
        ('MG', 'Miligrama (mg)'),
        ('LTR', 'Litro (l)'),
        ('ML', 'Mililitro (ml)'),
        ('PCT', 'Pacote (pct)'),
        ('UN', 'Unidade (und)'),
    )

    unidadeOrganizacao = models.ForeignKey(
        UnidadeOrganizacao, 
        on_delete=models.PROTECT, 
        db_column='unidade_org_id', 
        default=1,
        verbose_name='Unidade Organização',
    )
    descricao = models.CharField(
        max_length=50, 
        verbose_name='Descrição',
        help_text='Informe a descrição do grupo',
    )
    unidadeEmbalagem = models.CharField(
        max_length=5, 
        choices=UNIDADE_CHOICES, 
        blank=False, 
        null=False, 
        db_column='unidade_embalagem', 
        verbose_name='Unidade Embalagem',
        help_text='Informe a unidade de embalagem do grupo',
    )
    qtdeNaEmbalagem = models.DecimalField(
        max_digits=8, 
        decimal_places=3, 
        db_column='qtde_na_embalagem', 
        default=1, 
        validators=[MinValueValidator(Decimal(0.001))], 
        verbose_name='Qtde na Embalagem',
        help_text='Informe a quantidade na embalagem',
    )
    unidadesNaCesta = models.PositiveSmallIntegerField(
        db_column='unidades_na_cesta', 
        default=1, 
        null=False, 
        validators=[MinValueValidator(1)],
        verbose_name='Unidades na Cesta',
        help_text='Informe a quantidade que vai na cesta',
    )
    compoeCesta = models.BooleanField(
        db_column='compoe_cesta', 
        default=True, 
        verbose_name='Item Compõe a Cesta?',
    )
    diasValidadeMinima = models.PositiveSmallIntegerField(
        db_column='dias_validade_minima',
        default=10,
        null=False,
        validators=[MinValueValidator(1)],
        verbose_name='Validade Mínima',
        help_text='Informe em dias a validade mínima para cesta',
    )

    def __str__(self):
        return self.descricao.strip() + ' (' + self.unidadeEmbalagem + ')'

class Produto(models.Model):

    unidadeOrganizacao = models.ForeignKey(
        UnidadeOrganizacao, 
        on_delete=models.PROTECT, 
        db_column='unidade_org_id', 
        default=1,
        verbose_name='Unidade Organização',
    )
    descricao = models.CharField(
        max_length=50, 
        verbose_name='Descrição',
        help_text='Informe a descrição do produto',
    )
    grupoProduto = models.ForeignKey(GrupoProduto, 
        on_delete=models.PROTECT, 
        db_column='grupo_produto_id', 
        verbose_name='Grupo',
        help_text='Selecione o grupo do produto',
    )
    qtdeNaEmbalagem = models.DecimalField(
        max_digits=8, 
        decimal_places=3, 
        db_column='qtde_na_embalagem', 
        default=1, 
        validators=[MinValueValidator(Decimal(0.001))], 
        verbose_name='Qtde na Embalagem',
        help_text='Informe a quantidade na embalagem',
    )
    aceitaDoacao = models.BooleanField(
        db_column='aceita_doacao', 
        default=True, 
        verbose_name='Aceita Doação?',
    )

    def __str__(self):
        return self.descricao

class DoacaoAgendada(models.Model):

    STATUS_CHOICES = (
        ('PEN', 'Pendente'),
        ('REC', 'Recebido'),
        ('CAN', 'Cancelado'),
    )

    unidadeOrganizacao = models.ForeignKey(
        UnidadeOrganizacao, 
        on_delete=models.PROTECT, 
        db_column='unidade_org_id', 
        default=1,
        verbose_name='Unidade Organização',
    )
    doador = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        db_column='doador_user_id',
        verbose_name='Doador',
    )
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.PROTECT, 
        db_column='produto_id',
        verbose_name='Produto',
        help_text='Selecione o produto que foi doado',
    )
    dataAgendamento = models.DateField(
        db_column='data_agendamento',
        verbose_name='Data Agendamento',
        auto_now_add=True,
    )
    quantidade = models.PositiveSmallIntegerField(
        db_column='qtde_agendada', 
        default=1,
        verbose_name='Quantidade',
        validators=[MinValueValidator(1)],
    )
    status = models.CharField(
        max_length=5, 
        choices=STATUS_CHOICES, 
        blank=False, 
        null=False, 
        default=STATUS_CHOICES[0][0],
        verbose_name='Status',
    )
    
    def __str__(self):
        return self.produto.descricao + ' em ' + self.dataAgendamento.strftime('%d/%m/%Y')

class DoacaoRecebida(models.Model):

    DIAS_INICIO_PERIODO = 60

    STATUS_CHOICES = (
        ('EST', 'Estoque'),
        ('ENT', 'Entregue'),
        ('PER', 'Perda'),
    )

    unidadeOrganizacao = models.ForeignKey(
        UnidadeOrganizacao, 
        on_delete=models.PROTECT, 
        db_column='unidade_org_id', 
        default=1,
        verbose_name='Unidade Organização',
    )
    doador = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        db_column='doador_user_id',
        verbose_name='Doador',
        help_text='Selecione o doador. Em branco se não identificado',
        blank=True,
        null=True,
    )
    dataRecebimento = models.DateField(
        db_column='data_recebimento',
        default=date.today,
        verbose_name='Data Recebimento',
        validators=[MaxValueValidator(limit_value=date.today)],
        help_text='Informe uma data menor ou igual a data atual',
    )
    dataBaixa = models.DateField(
        db_column='data_baixa',
        verbose_name='Data da Baixa',
        help_text='Informe uma data menor ou igual a data atual',
        blank=True,
        null=True,
        validators=[MaxValueValidator(limit_value=date.today)],
    )
    produto = models.ForeignKey(
        Produto, 
        db_column='produto_id',
        on_delete=models.PROTECT,
        verbose_name='Produto',
        help_text='Selecione o produto que foi doado',
    )
    quantidade = models.PositiveSmallIntegerField(
        db_column='qtde_recebida', 
        default=1,
        verbose_name='Quantidade',
        help_text='Informe o número de unidades doadas',
        validators=[MinValueValidator(1)],
    )
    doacaoAgendada = models.ForeignKey(
        DoacaoAgendada, 
        db_column='doacao_agendada_id',
        on_delete=models.PROTECT, 
        verbose_name='Doação Agendada',
        blank=True,
        null=True,
    )
    dataValidade = models.DateField(
        db_column='data_validade',
        verbose_name='Data Validade',
        help_text='Informe a data de validade do produto',
        validators=[MinValueValidator(limit_value=date.today)],
    )
    status = models.CharField(
        max_length=5, 
        choices=STATUS_CHOICES, 
        verbose_name='Status',
        default=STATUS_CHOICES[0][0],
        blank=False, 
        null=False, 
    )
    doacaoViaWeb = models.BooleanField(
        db_column='doacao_via_web', 
        default=True,
        verbose_name='Doação via Web?',
    )
    saldoDeEntrega = models.BooleanField(
        db_column='saldo_de_entrega', 
        default=False,
        verbose_name='Saldo de Entrega?',
    )

    def __str__(self):
        return self.produto.descricao + ' em ' + self.dataRecebimento.strftime('%d/%m/%Y')
