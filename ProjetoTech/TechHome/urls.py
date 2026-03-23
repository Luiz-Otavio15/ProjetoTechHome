from . import views
from django.urls import path
app_name = "TechHome"

urlpatterns = [
    path('', views.tela_principal_tech, name='tela_principal' )
]
