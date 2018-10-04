from django.forms import ModelForm
from .models import ContasTransacao, ContasCategoria, ContasClientes, AuthUser
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
        authenticate,
        get_user_model

    )

User = get_user_model()

class TransacaoForm(ModelForm):
    class Meta:
        model = ContasTransacao
        fields = ['descricao','valor','categoria','observacoes']


class CategoriaForm(ModelForm):
    class Meta:
        model = ContasCategoria
        fields = ['nome']


class ClientesForm(ModelForm):  
    class Meta:
        model = AuthUser
        fields = ['username','first_name','last_name','email','password']

        widgets = {
            'password':forms.PasswordInput()
        }
        
       
