from . import views
from django.urls import path

urlpatterns = [
    path('', views.tela_principal_tech, name='tela_principal' ),
]
