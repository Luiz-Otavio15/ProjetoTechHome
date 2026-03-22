from django.shortcuts import render

from .models import *

# Create your views here.

def tela_principal_tech(request):
    produtos = Produto.objects.all()
    return render(request, 'html/Tela1Home.html', {'produtos': produtos})