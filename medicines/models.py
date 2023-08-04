from django.db import models

class Medicines(models.Model):
    id = models.AutoField(primary_key=True)
    principio_ativo = models.CharField(max_length=1000, default='null')
    nome_comercial = models.CharField(max_length=1000, default='null')
    classe_droga = models.CharField(max_length=1000, default='null')
    nome_cientifico = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    composicao = models.CharField(max_length=1000)
    usos = models.CharField(max_length=1000)
    contra_indicacoes = models.CharField(max_length=1000)
    doencas_situacoes = models.CharField(max_length=1000)
    faq = models.CharField(max_length=1000)
    upload = models.FileField(upload_to='uploads/')
    
    class Meta:
        db_table = 'medicines'
