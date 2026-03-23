from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import *

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

def tela_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        Suporte.objects.create(
            nome=nome,
            assunto=assunto,
            mensagem=mensagem
        )
        return render(request, 'html/Tela2_contato.html', {'sucesso': True})
    else:
        return render(request, 'html/Tela2_Contato.html')   


    



