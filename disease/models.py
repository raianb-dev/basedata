from django.db import models

    
class Doenca (models.Model):

    id = models.IntegerField(primary_key=True)
    nome_comum = models.CharField(max_length=500)
    termo_medico = models.CharField(max_length=500)
    descricao = models.CharField(max_length=500)
    causa = models.CharField(max_length=500)
    prevencao = models.CharField(max_length=500)
    sinal_sintoma = models.CharField(max_length=500)
    fator_risco = models.CharField(max_length=500)
    diagnostico_tratamento = models.CharField(max_length=500)
    medidas_gerais = models.CharField(max_length=500)
    medicamentos_gerais = models.CharField(max_length=500)
    dieta = models.CharField(max_length=500)
    prognostico = models.CharField(max_length=500)
    suplemento = models.CharField(max_length=500)
    faq_doença = models.CharField(max_length=500)
    referencia = models.CharField(max_length=500)

    class Meta:
        db_table = 'doenca'
