from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import TransacaoForm 

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t2']
    data['dinheiro'] = ['a1','a2','a3']
    data['nomes']=['Hugo','Monielle','Pedro']

    data['now'] = datetime.datetime.now()

    return render(request, 'contas/home.html', data)

def login(request):

    return render(request, 'contas/login.html')

def nova_transacao(request):
    #instanciamos do "from .foms import TransacaoForm"
    data = {}
    #sempre que chamar o model do form tem que colocar ()
    form = TransacaoForm()
    data['form'] = form
    
    # passa o form para a view chamaada form.html pelo data
    return render(request, 'contas/form.html', data)
