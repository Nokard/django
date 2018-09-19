from django.db import models
from django.forms import CharField, Form, PasswordInput

# Create your models here.

#Depois que criar os models do banco de dados sempre usar o "python manage.py makemigrations"
# e depois "python manage.py migrate"
#Para concluir no banco 

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits= 7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True)

    def __str__(self):
        return self.descricao  

class Clientes(models.Model):
    nome = models.CharField(max_length=85)
    email = models.EmailField(max_length=85)
    senha = models.CharField(max_length=30)
    teste = models.CharField(max_length=85, null=True)

#Classe Documento tem relacionamento com a Person ONE TO ONE 
class Documento(models.Model):
    num_doc = models.CharField(max_length=50)
    
    #função usada para retornar a numero em forma de text
    def __str__(self):
            return self.num_doc

#Classe pessoa que tem relacao com a classe Documento One to One
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField()
