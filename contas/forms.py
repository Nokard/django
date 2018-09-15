from django.forms import ModelForm
from .models import Transacao

class TransacaoForm(ModelForm):
    class meta:
        model = Transacao
        fields = ['data','descricao','valor','categoria','observacoes']
