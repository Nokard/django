from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t2']
    data['dinheiro'] = ['a1','a2','a3']
    data['nomes']=['Hugo','Monielle','Pedro']

    data['now'] = datetime.datetime.now()

    return render(request, 'contas/home.html', data)

def login(request):

    return render(request, 'contas/login.html')
