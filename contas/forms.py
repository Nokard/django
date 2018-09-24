from django.forms import ModelForm
from .models import Transacao, Categoria, Clientes
from django import forms
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import (
        authenticate,
        get_user_model

    )

User = get_user_model()

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao','valor','categoria','observacoes']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class ClientesForm(ModelForm):  
    class Meta:
        model = Clientes
        fields = ['nome','email','senha','senha2','descricao']
        
        widgets = {
            'senha':forms.PasswordInput()
        }

class loginClient(ModelForm):
    class Meta:
        model = Clientes
        fields = ['email','senha']
        
        widgets = {
            'senha':forms.PasswordInput()
        }