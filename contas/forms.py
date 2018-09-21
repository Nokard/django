from django.forms import ModelForm
from .models import Transacao, Categoria, Clientes
from django import forms
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import authenticate


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

    #Essa funcao limpa os campos username e password
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            #para usar o authentication precisa importar from django.contrib.auth import authenticate
            user = authenticate(username=username,  password=password)
            if not user:
                raise forms.ValidationError('Esse usuario não existe')
            if not user.check_password(password):
                raise forms.ValidationError('Senha errada')
            if not user.is_activate:
                raise forms.ValidationError('Nao esta autenticacdo')
        return super()


