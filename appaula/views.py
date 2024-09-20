from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Instituicao
from .forms import InstituicaoForm

#Metodo para abrir a página da Instituição para Novo cadastro ou Alteração de um existente
def criar_instituicao(request, id=None):
    print("cheguei aqui")
    instituicao = get_object_or_404(Instituicao, pk=id) if id else None
    lista_instituicoes = Instituicao.objects.all()
    if request.method == "POST":
        form = InstituicaoForm(request.POST, instance=instituicao)
        if form.is_valid():
            form.save()            
            return redirect('appaula/form_instituicao.html')  
    else:
        form = InstituicaoForm(instance=instituicao)
    
    return render(request, 'appaula/form_instituicao.html', {'form': form,'lista_instituicoes':lista_instituicoes})

#Metodo para listar as instituições cadastradas
def instituicao_list(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'instituicao_list.html', {'instituicoes': instituicoes})

#Metodo para lista os setores cadastrados
def setor_list(request):
    setores = Setor.objects.all()
    return render(request, 'setor_list.html', {'setores': setores})

# Create your views here.
#chama a pagina index
def index(request):

    return render(request,'appaula/index.html')

#chama a pagina cadastro_pessoa.html
def cadastro_pessoa(request):
    
    return render(request,'appaula/cadastro_pessoa.html')


