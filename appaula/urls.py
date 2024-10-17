from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),        
    path('instituicao/novo',views.criar_instituicao,name='criar_instituicao'),
    path('instituicao/alterar/<int:id>/', views.criar_instituicao, name='editar_instituicao'),
    path('instituicao/excluir/<int:id>/', views.excluir_instituicao, name='excluir_instituicao'),
    path('instituicoes/', views.listar_instituicoes, name='listar_instituicoes'),
    path('setores/', views.listar_setores, name='listar_setores'),
    path('setor/alterar/<int:id>/', views.criar_setor, name='editar_setor'),
    path('setor/excluir/<int:id>/', views.excluir_setor, name='excluir_setor'),
    path('setor/novo',views.criar_setor,name='criar_setor'),    
    path('pessoa/novo',views.criar_pessoa,name="criar_pessoa"),
    path('pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('pessoa/alterar/<int:id>/', views.criar_pessoa, name='editar_pessoa'),
    path('pessoa/excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),    
    path('lotacao/novo',views.criar_lotacao,name="criar_lotacao"),
    path('lotacoes/', views.listar_lotacoes, name='listar_lotacoes'),
    path('lotacao/alterar/<int:id>/', views.criar_lotacao, name='editar_lotacao'),
]

