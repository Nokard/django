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

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

