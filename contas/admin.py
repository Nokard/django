from django.contrib import admin
from .models import Categoria, Transacao, Clientes

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Clientes)
