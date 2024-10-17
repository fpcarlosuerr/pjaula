from django.contrib import admin
from .models import Instituicao

# Register your models here.

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia','cnpj')
    search_fields = ('nome_fantasia','cnpj')
    