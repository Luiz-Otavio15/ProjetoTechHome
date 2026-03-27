from . import views
from django.urls import path
app_name = "TechHome"

urlpatterns = [
    path('', views.tela_principal_tech, name='tela_principal' ),
    path('contato/', views.tela_contato, name='tela_contato'),
    path('produtos/', views.tela_categoria, name='tela_categoria'),
    path('produto/<int:id>/', views.tela_detalhes, name='tela_detalhes'),
    path('comprar/<int:id>/', views.tela_compra, name='tela_compra')
]
