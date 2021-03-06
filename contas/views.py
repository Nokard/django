from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms 
from .models import ContasClientes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
from .forms import TransacaoForm, CategoriaForm, ClientesForm
# login_required é usado para fazer verificar a validacao do login nas paginas @login_required

def home(request):
    
    return render(request, 'contas/home.html')


@login_required
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

#Serve para verificar se existe um usuario logado na página
@login_required
def novaCategoria(request):

    catForm = CategoriaForm()
    catForm = CategoriaForm(request.POST or None)

    if catForm.is_valid():
        catForm.save()

    return render(request, 'contas/formCat.html', {'catForm': catForm})


def cadastroCli(request):

    cadastroForm = ClientesForm()
    cadastroForm = ClientesForm(request.POST or None)

    if cadastroForm.is_valid():
        cadastroForm.save()

    return render(request, 'contas/cadastoClie.html', {'cadClie': cadastroForm})


@login_required
def index(request):
    pesquisa = request.GET.get('pesquisa', None)

    if pesquisa:
        clientes = ContasClientes.objects.filter(cnpj=pesquisa)
    else:
        clientes = ContasClientes.objects.all()
    
    return render(request, 'contas/index.html', {'clientes': clientes})

def do_logout(request):
    logout(request)
    return redirect('home')

