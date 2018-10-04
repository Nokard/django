# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(default='0')
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField(default='0')
    is_active = models.IntegerField(default='1')
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ContasArticle(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'contas_article'


class ContasCategoria(models.Model):
    nome = models.CharField(max_length=200)
    dt_criacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contas_categoria'


class ContasClientes(models.Model):
    nome = models.CharField(max_length=85, blank=True, null=True)
    email = models.CharField(max_length=85)
    senha = models.CharField(max_length=85)
    descricao = models.CharField(max_length=85, blank=True, null=True)
    cnpj = models.BigIntegerField(blank=True, null=True)
    nomeempresa = models.CharField(db_column='nomeEmpresa', max_length=85, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_clientes'


class ContasDocumento(models.Model):
    num_doc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'contas_documento'


class ContasPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'contas_person'


class ContasTransacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(ContasCategoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contas_transacao'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class End(models.Model):
    rua = models.CharField(max_length=85, blank=True, null=True)
    cidade = models.CharField(max_length=85, blank=True, null=True)
    bairro = models.CharField(max_length=85, blank=True, null=True)
    uf = models.CharField(max_length=85, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'end'


class Nome(models.Model):
    nome = models.CharField(max_length=11, blank=True, null=True)
    sob = models.CharField(max_length=45, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nome'
