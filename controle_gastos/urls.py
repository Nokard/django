from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from contas.views import home, novaTransacao, novaCategoria, cadastroCli, index, loginCliente


urlpatterns = [
    path('', home),
    path('login/', loginCliente, name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('index/form/', novaTransacao),
    path('index/catform/', novaCategoria),
    path('cadastro/', cadastroCli),
    path('index/', index),
    #path('login/', auth_views.login, name='login'),
    

    
]
