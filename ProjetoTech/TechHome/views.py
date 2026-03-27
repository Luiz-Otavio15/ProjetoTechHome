from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

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
        return render(request, 'html/Tela2_Contato.html', {'sucesso': True})
    else:
        return render(request, 'html/Tela2_Contato.html')   


    
def tela_categoria(request):
    produtos = Produto.objects.all()
    categoria = request.GET.get('categoria')
    

    if categoria:
        produtos = produtos.filter(categoria__nome=categoria)

    return render(request, 'html/Tela3Categoria.html', {'produto':produtos})

def tela_detalhes(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    return render(request, 'html/Tela4Detalhes.html', {'produto':produto})

def tela_compra(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.estoque -= 1
        produto.save()
        if produto.estoque == 0:
            produto.delete()
    else:
        print("Produto sem estoque")
    return redirect("TechHome:tela_principal")