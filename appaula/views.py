from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Instituicao
from .forms import InstituicaoForm

#Metodo para abrir a página da Instituição para Novo cadastro ou Alteração de um existente
def criar_instituicao(request, id=None):
    # Se 'id' for fornecido, buscar a Instituição específica, senão, criar nova
    instituicao = get_object_or_404(Instituicao, pk=id) if id else None
    lista_instituicoes = Instituicao.objects.all()

    if request.method == "POST":
        form = InstituicaoForm(request.POST, instance=instituicao)
        if form.is_valid():
            form.save()
            if instituicao:
                messages.success(request, 'Instituição atualizada com sucesso!')
            else:
                messages.success(request, 'Instituição adicionada com sucesso!')

            return redirect('listar_instituicoes')  # Redirecionar para a view de listagem
    else:
        form = InstituicaoForm(instance=instituicao)

    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao
    })
    
#Metodo para listar as instituições cadastradas
def listar_instituicoes(request):
    instituicao = None
    lista_instituicoes = Instituicao.objects.all()
    form = InstituicaoForm(instance=instituicao)
    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao})


# Create your views here.
#chama a pagina index
def index(request):

    return render(request,'appaula/index.html')

#chama a pagina cadastro_pessoa.html
def cadastro_pessoa(request):
    
    return render(request,'appaula/cadastro_pessoa.html')


