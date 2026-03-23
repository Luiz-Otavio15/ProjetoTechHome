from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Produto

# Create your views here.

def tela_principal_tech(request):
    produtos = Produto.objects.all()
    barra = request.GET.get('barra')

    if barra:
        produtos = produtos.filter(nome__icontains=barra)


    return render(request, 'html/Tela1Home.html', {
        'produtos': produtos,
        'barra': barra
        },)