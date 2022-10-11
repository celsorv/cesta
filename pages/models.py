from django.db import models
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


class GrupoProduto(models.Model):

    TIPOS_UNITARIOS = (
        ('UN', 'Unitario'),
        ('KG', 'KiloGrama'),
        ('L', 'Litro'),
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
        choices=TIPOS_UNITARIOS, 
        blank=False, 
        null=False, 
        db_column='unidade_embalagem', 
        verbose_name='Unidade Embalagem',
        help_text='Informe a unidade de embalagem do grupo',
    )
    unidadesNaCesta = models.DecimalField(
        max_digits=8, 
        decimal_places=3, 
        db_column='unidades_na_cesta', 
        default=1, 
        null=False, 
        blank=False,
        validators=[MinValueValidator(Decimal(0.001))],
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
    qtdeNaEmbalagem = models.DecimalField(
        max_digits=8, 
        decimal_places=3, 
        db_column='qtde_na_embalagem', 
        default=1, 
        validators=[MinValueValidator(Decimal(0.001))], 
        verbose_name='Qtde na Embalagem',
        help_text='Informe a quantidade na embalagem',
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
    TIPOS_UNITARIOS = (
        ('UN', 'Unitario'),
        ('KG', 'KiloGrama'),
        ('L', 'Litro'),
    )
    tipo_unitario = models.CharField(
        max_length=5,
        choices=TIPOS_UNITARIOS,
        blank=False,
        null=False,
        default=TIPOS_UNITARIOS[0][0],
        verbose_name='TipoUnitario'
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
