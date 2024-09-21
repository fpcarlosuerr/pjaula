from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),    
    path('cadastro_pessoa',views.cadastro_pessoa,name="cadpessoa"),
    path('instituicao/novo',views.criar_instituicao,name='criar_instituicao'),
    path('instituicao/alterar/<int:id>/', views.criar_instituicao, name='editar_instituicao'),
    path('instituicoes/', views.listar_instituicoes, name='listar_instituicoes'),
]
