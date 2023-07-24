from django.db import models


class Saude(models.Model):

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=10000)
    action_mechanisms = models.CharField(max_length=10000)
    potential_benefits = models.CharField(max_length=10000)
    effects_precautions = models.CharField(max_length=10000)
    gene_interactions = models.CharField(max_length=10000)
    references = models.CharField(max_length=10000)
    user_experience = models.CharField(max_length=10000)
    scientific_studies = models.CharField(max_length=10000)
    faq = models.CharField(max_length=10000)

    class Meta:
        db_table = 'saude'  
