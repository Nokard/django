from django.db import models


# Create your models here.

#Depois que criar os models do banco de dados sempre usar o "python manage.py migrate"
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

