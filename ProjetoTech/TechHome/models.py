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

    def __str__(self):
        return self.nome
