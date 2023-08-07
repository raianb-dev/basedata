from django.db import models

class Habits(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000, default='null')
    beneficios = models.CharField(max_length=1000, default='null')
    equipamentos_requisitos = models.CharField(max_length=1000)
    como_fazer = models.CharField(max_length=1000)
    por_que_funciona = models.CharField(max_length=1000)
    tempo_estimado = models.CharField(max_length=1000)
    frequencia = models.CharField(max_length=1000)
    hora_do_dia = models.CharField(max_length=1000)
    efeitos = models.CharField(max_length=1000)
    dicas = models.CharField(max_length=1000)

    class Meta:
        db_table = 'habits'
