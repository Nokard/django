from django.forms import ModelForm
from .models import Transacao, Categoria, Clientes
from django import forms
from django.contrib.auth.decorators import login_required
from django import forms



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
        fields = ['nome','email','senha']
        
        widgets = {
            'senha':forms.PasswordInput()
        }

class HomeForm(forms.Form):
    nome = forms.CharField(label = 'Nome', max_length=85)