from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Instituicao, Setor, Pessoa, Lotacao
from .forms import InstituicaoForm, SetorForm, PessoaForm, LotacaoForm
from django.db import connections


#Metodo para abrir a página da Instituição para Novo cadastro ou Alteração de um existente
def criar_instituicao(request, id=None):
    # Para pesquisar todos os objetos da classe Instituicao em ordem decrescente de id, você pode usar o método order_by() no Django ORMSe 'id' for fornecido, buscar a Instituição específica, senão, criar nova
    instituicao = get_object_or_404(Instituicao, pk=id) if id else None
    
    #Para pesquisar todos os objetos da classe Instituicao em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_instituicoes = Instituicao.objects.all().order_by('-id')

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

def excluir_instituicao(request, id):
    instituicao = get_object_or_404(Instituicao,pk=id)
    instituicao.delete()
    instituicao=None
    
    #Para pesquisar todos os objetos da classe Instituicao em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_instituicoes=Instituicao.objects.all().order_by('-id')
    
    form = InstituicaoForm(instance=instituicao)
    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao
    })
    
#Metodo para listar as instituições cadastradas
def listar_instituicoes(request):
    instituicao = None
    
    #Para pesquisar todos os objetos da classe Instituicao em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_instituicoes = Instituicao.objects.all().order_by('-id')
    
    form = InstituicaoForm(instance=instituicao)
    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao})


#Metodo para abrir a página da Setor para Novo cadastro ou Alteração de um existente
def criar_setor(request, id=None):
    # Para pesquisar todos os objetos da classe Setor em ordem decrescente de id, você pode usar o método order_by() no Django ORMSe 'id' for fornecido, buscar a Setor específica, senão, criar nova
    setor = get_object_or_404(Setor, pk=id) if id else None
    
    #Para pesquisar todos os objetos da classe Setor em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_setores = Setor.objects.all().order_by('-id')

    if request.method == "POST":
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            if setor:
                messages.success(request, 'Setor atualizada com sucesso!')
            else:
                messages.success(request, 'Setor adicionado com sucesso!')

            return redirect('listar_setores')  # Redirecionar para a view de listagem
    else:
        form = SetorForm(instance=setor)

    return render(request, 'appaula/form_setor.html', {
        'form': form,
        'lista_setores': lista_setores,
        'setor': setor
    })

#Metodo para listar as Setores cadastrados
def listar_setores(request):
    setor = None
    
    #Para pesquisar todos os objetos da classe Instituicao em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_setores = Setor.objects.all().order_by('-id')
    
    form = SetorForm(instance=setor)
    return render(request, 'appaula/form_setor.html', {
        'form': form,
        'lista_setores': lista_setores,
        'setor': setor})


def excluir_setor(request, id):
    setor = get_object_or_404(Setor,pk=id)
    setor.delete()
    setor=None
    
    #Para pesquisar todos os objetos da classe Instituicao em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_setores=Setor.objects.all().order_by('-id')
    
    form = SetorForm(instance=setor)
    return render(request, 'appaula/form_setor.html', {
        'form': form,
        'lista_setores': lista_setores,
        'setor': setor
    })

# Create your views here.
#chama a pagina index
def index(request):

    return render(request,'appaula/index.html')

#chama a pagina form_pessoa.html
#Metodo para abrir a página de Pessoa para Novo cadastro ou Alteração de um existente
def criar_pessoa(request, id=None):
    # Se 'id' for fornecido, buscar a Pessoa específica, senão, criar nova
    pessoa = get_object_or_404(Pessoa, pk=id) if id else None

    # Listar todas as pessoas em ordem decrescente de ID
    lista_pessoas = Pessoa.objects.all().order_by('-id')

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            if pessoa:
                messages.success(request, 'Pessoa atualizada com sucesso!')
            else:
                messages.success(request, 'Pessoa adicionada com sucesso!')
            return redirect('listar_pessoas')  # Redirecionar após a criação ou atualização
        else:
            # Exibir mensagens de erro para cada campo
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'appaula/form_pessoa.html', {
        'form': form,
        'lista_pessoas': lista_pessoas,
        'pessoa': pessoa
    })


def listar_pessoas(request):
    # Listar todas as pessoas em ordem decrescente de ID
    lista_pessoas = Pessoa.objects.all().order_by('-id')

    return render(request, 'appaula/form_pessoa.html', {
        'lista_pessoas': lista_pessoas,
    })


def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    pessoa.delete()
    messages.success(request, 'Pessoa excluída com sucesso!')

    return redirect('listar_pessoas')  # Redirecionar para a listagem após a exclusão


#chama a pagina form_lotacao.html
#Metodo para abrir a página de Pessoa para Novo cadastro ou Alteração de um existente
def criar_lotacao(request, id=None):
    # Para pesquisar todos os objetos da classe Setor em ordem decrescente de id, você pode usar o método order_by() no Django ORMSe 'id' for fornecido, buscar a Setor específica, senão, criar nova
    lotacao = get_object_or_404(Lotacao, pk=id) if id else None
    
    #Para pesquisar todos os objetos da classe Pessoa em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_lotacoes = Lotacao.objects.all().order_by('-id')    

    if request.method == "POST":        
        form = LotacaoForm(request.POST, instance=lotacao)             
        if form.is_valid():
           form.save()            
           if lotacao:
              messages.success(request, 'Lotação atualizada com sucesso!')                
           else:
              messages.success(request, 'Lotação adicionado com sucesso!')
              return redirect('listar_lotacoes')  # Redirecionar para a view de listagem
        else:
           for field, errors in form.errors.items():
               for error in errors:
                   messages.error(request, f"Erro no campo {field}: {error}")
    else:                
        form = LotacaoForm(instance=lotacao)
    return render(request, 'appaula/form_lotacao.html', {
        'form': form,
        'lista_lotacoes': lista_lotacoes,
        'lotacao': lotacao
    })    

#Metodo para listar as Pessoas cadastrados
def listar_lotacoes(request):
    lotacao = None
    
    #Para pesquisar todos os objetos da classe Pessoa em ordem decrescente de id, você pode usar o método order_by() no Django ORM
    # o -id indica que a ordenação deve ser feita de forma decrescente com base no campo id
    lista_lotacoes = Lotacao.objects.all().order_by('-id')
    
    form = LotacaoForm(instance=lotacao)
    return render(request, 'appaula/form_lotacao.html', {
        'form': form,
        'lista_lotacoes': lista_lotacoes,
        'lotacao': lotacao})

def excluir_lotacao(request, id):
    lotacao = get_object_or_404(Lotacao, pk=id)
    lotacao.delete()
    messages.success(request, 'Lotação excluída com sucesso!')
    return redirect('listar_lotacoes')  # Redirecionar para a listagem de lotações

def abrir_lista_pessoas(request):
    lista_pessoas=get_lista_pessoa()
    print(get_pessoa_pelo_id(5))
    return render(request,'appaula/relatorio_de_pessoas.html',
                  {
                      'lista_pessoas':lista_pessoas
                  })

def get_lista_pessoa():
    with connections['default'].cursor() as cursor:
        sql = """
            select a.nome_fantasia instituicao, b.nome setor, d.nome, d.cpf 
                from appaula_instituicao a
                join appaula_setor b on b.instituicao_id =a.id
                join appaula_lotacao c on c.setor_id =b.id 
                join appaula_pessoa d on d.id =c.pessoa_id 
         """
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        lista = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return lista

def get_pessoa_pelo_id(id):
    with connections['default'].cursor() as cursor:
        sql = """
            select a.nome_fantasia instituicao, b.nome setor, d.nome, d.cpf 
                from appaula_instituicao a
                join appaula_setor b on b.instituicao_id =a.id
                join appaula_lotacao c on c.setor_id =b.id 
                join appaula_pessoa d on d.id =c.pessoa_id
            where d.id = %s 
         """
        cursor.execute(sql,[id])
        columns = [col[0] for col in cursor.description]
        lista = [dict(zip(columns, row)) for row in cursor.fetchall()]


    return lista