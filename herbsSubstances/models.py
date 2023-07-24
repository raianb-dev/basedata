from django.db import models

class herbsSubstance(models.Model):

    id = models.AutoField(primary_key=True)
    resumo = models.CharField(max_length=10000)
    oque_e = models.CharField(max_length=10000)
    beneficios = models.CharField(max_length=10000)
    boa_para_que = models.CharField(max_length=10000)
    doencas_relacionada = models.CharField(max_length=10000)
    desvantagens_cuidados = models.CharField(max_length=10000)
    como_funciona = models.CharField(max_length=10000)
    dosagem = models.CharField(max_length=10000)
    faq = models.CharField(max_length=10000)
    estudos = models.CharField(max_length=10000)

    class Meta:
        db_table = 'substancia_ervas'  
