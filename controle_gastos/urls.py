from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path,include
from contas.views import home, novaTransacao, novaCategoria, cadastroCli, index, do_logout

urlpatterns = [
    path('', home, name="home"),
    path('login/', LoginView.as_view(), name='login'),
    #path('index/sair/', LogoutView.as_view(), {'next_page': 'contas/home.html/'}, name = 'logout'),
    path('logout/', do_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('index/form/', novaTransacao),
    path('index/catform/', novaCategoria),
    path('cadastro/', cadastroCli),
    path('index/', index, name='index'),
    #path('login/', auth_views.login, name='login'),
        
]
