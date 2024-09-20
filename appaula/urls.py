from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),    
    path('cadastro_pessoa',views.cadastro_pessoa,name="cadpessoa"),
    path('instituicao/novo',views.criar_instituicao,name='criar_instituicao'),
]
