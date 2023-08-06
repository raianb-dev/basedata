from django.db import models

class Blog(models.Model):

    id = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'blog'