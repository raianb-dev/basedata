# Generated by Django 3.1 on 2023-07-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saude',
            name='name',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
