from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#chama a pagina index
def index(request):

    return render(request,'appaula/index.html')

#chama a pagina cadastro_pessoa.html
def cadastro_pessoa(request):
    
    return render(request,'appaula/cadastro_pessoa.html')