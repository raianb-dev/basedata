# Generated by Django 3.1 on 2023-07-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='herbsSubstance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resumo', models.CharField(max_length=10000)),
                ('oque_e', models.CharField(max_length=10000)),
                ('beneficios', models.CharField(max_length=10000)),
                ('boa_para_que', models.CharField(max_length=10000)),
                ('doencas_relacionada', models.CharField(max_length=10000)),
                ('desvantages_cuidados', models.CharField(max_length=10000)),
                ('como_funciona', models.CharField(max_length=10000)),
                ('dosagem', models.CharField(max_length=10000)),
                ('faq', models.CharField(max_length=10000)),
                ('estudos', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'substancia_ervas',
            },
        ),
    ]
