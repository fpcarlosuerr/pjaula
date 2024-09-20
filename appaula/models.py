from django.db import models

# Create your models here.

#Classe Instituição
class Instituicao(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome_fantasia

class Setor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ramal = models.CharField(max_length=20)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_de_nascimento =models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    cep = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.nome

class Lotacao(models.Model):
   pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)     
   setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
   data_entrada=models.DateField()
   data_saida = models.DateField(null=True, blank=True)
   situacao = models.IntegerField()
   
   def __str__(self):
       return f"{self.pessoa.nome} - {self.setor.nome}"