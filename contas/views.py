from django.shortcuts import render 
from django.http import HttpResponse
import datetime
from .forms import TransacaoForm, CategoriaForm

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t2']
    data['dinheiro'] = ['a1','a2','a3']
    data['nomes']=['Hugo','Monielle','Pedro']

    data['now'] = datetime.datetime.now()

    return render(request, 'contas/home.html', data)

def login(request):

    return render(request, 'contas/login.html')


def novaTransacao(request):

        form = TransacaoForm()
        # Verificando se já veio com o dados (Preenchida) pelo POST
        form = TransacaoForm(request.POST or None)
 
        if form.is_valid():
            form.save()

        #instanciamos do "from .foms import TransacaoForm"
        #sempre que chamar o model do form tem que colocar () 
        # passa o form para a view chamaada form.html pelo data
        return render(request, 'contas/form.html', {'form': form})

def novaCategoria(request):

    catForm = CategoriaForm()
    catForm = CategoriaForm(request.POST or None)

    if catForm.is_valid():
        catForm.save()

    return render(request, 'contas/formCat.html', {'catForm': catForm})