from django import forms
from .models import Instituicao, Setor


class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome_fantasia','cnpj']
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
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'ramal':forms.TextInput(attrs={'class':'form-control'}),
            'instituicao':forms.Select(attrs={'class':'form-control'}),            
        }