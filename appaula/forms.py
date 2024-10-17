from django import forms
from .models import Instituicao, Setor, Pessoa, Lotacao


class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome_fantasia','cnpj']
        labels = {
            'nome_fantasia':'Nome fantasia da instituição',
            'cnpj':'CNPJ da instituição'
        }
        widgets = {
            'nome_fantasia':forms.TextInput(attrs={'class':'form-control','required': 'required'}),
            'cnpj':forms.TextInput(attrs={'class':'form-control'}),                            
        }
        # error_messages = {
        #     'nome_fantasia': {
        #         'required': 'O campo "Nome Fantasia" é obrigatório.',
        #     },
        #     'cnpj': {
        #         'required': 'O campo "CNPJ" é obrigatório.',
        #     },
        # }

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome','email','ramal','instituicao']
        labels = {
            'instituicao':'Nome da Instituição',
            'nome':'Nome do Setor',
            'email':'E-Mail do Setor',
            'ramal':'Ramal do Setor',
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'ramal':forms.TextInput(attrs={'class':'form-control'}),
            'instituicao':forms.Select(attrs={'class':'form-control'}),            
        }

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'data_de_nascimento', 'telefone', 'email', 'cep']
        labels = {
            'nome':'Nome da Pessoa',
            'cpf':'CPF da Pessoa',
            'data_de_nascimento':'Data de Nascimento',
            'telefone':'Telefone',
            'email':'E-Mail',
            'cep':'cep'            
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'cpf':forms.TextInput(attrs={'class':'form-control'}),
            'data_de_nascimento':forms.DateInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'cep':forms.TextInput(attrs={'class':'form-control'}),
        }

from django import forms
from .models import Lotacao  # Certifique-se de importar o seu modelo Lotacao

class LotacaoForm(forms.ModelForm):
    # Definindo o campo 'situacao' como um BooleanField
    situacao = forms.BooleanField(
        required=False,  # Se você quiser que este campo seja opcional
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    class Meta:
        model = Lotacao        
        fields = ['pessoa', 'setor', 'data_entrada', 'data_saida', 'situacao']
        labels = {
            'pessoa': 'Identificação da Pessoa',
            'setor': 'Identificação do Setor de uma Instituição para Lotação',
            'data_entrada': 'Data da Lotação no Setor/Instituição',
            'data_saida': 'Data da saída do Setor/Instituição',
            'situacao': 'Situação Atual da Lotação (Ativo/Inativo)'
        }
        widgets = {
            'pessoa': forms.Select(attrs={'class': 'form-control'}),
            'setor': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada': forms.DateInput(attrs={'class': 'form-control'}),
            'data_saida': forms.DateInput(attrs={'class': 'form-control'}),
            # Não adicione o situacao aqui, pois já foi definido acima
        }
        
        