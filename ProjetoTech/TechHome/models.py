from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=220)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=220)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem =  models.ImageField(upload_to='fotos_produto/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome


class Suporte(models.Model):
    nome = models.CharField(max_length=100)
    motivo = models.TextField(max_length=100)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    ...

class Pedido(models.Model):
    ...