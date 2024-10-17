from django import forms
from .models import Instituicao, Setor, Lotacao, Pessoa


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


class LotacaoForm(forms.ModelForm):
    class Meta:
        model = Lotacao
        fields = ['pessoa', 'setor', 'data_entrada', 'data_saida', 'situacao']
        widgets = {
            'pessoa': forms.Select(attrs={'class': 'form-control'}),
            'setor': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'situacao': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'pessoa':'Nome da Pessoa',
            'setor': 'Setor da Instituição',
            'data_entrada': 'Data de Entrada no Setor',
            'data_saida': 'Data de Saída no Setor',
            'situacao': 'Situação da pessoa no setor',
        }


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa  # Certifique-se de que o modelo está especificado aqui
        fields = ['nome', 'cpf', 'data_de_nascimento', 'telefone', 'email', 'cep']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'data_de_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'data_de_nascimento': 'Data de Nascimento',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'cep': 'CEP',
        }
