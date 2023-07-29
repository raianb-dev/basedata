from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage

from herbsSubstances import models
from .models import herbsSubstance




def detalhes_item(request, item_id):
    herbsSubstances_item = get_object_or_404(herbsSubstance, id=item_id)
    return render(request, 'herbsSubstances_id.html', {'herbsSubstances_item': herbsSubstances_item})
    
def salvar_herbsSubstances(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        descricao = request.POST.get('descricao')
        oque_e = request.POST.get('oque_e')
        beneficio = request.POST.get('beneficio')
        potencial_beneficios = request.POST.get('potencial_beneficios')
        doencas_relacionadas = request.POST.get('doencas_relacionadas')
        como_funciona = request.POST.get('como_funciona')
        desvantagens = request.POST.get('desvantagens')
        dosagem = request.POST.get('dosagem')
        faq = request.POST.get('faq')
        estudos_cientificos = request.POST.get('estudos_cientificos')

        # Renomeie a variável local para evitar conflito com a classe herbsSubstance
        nova_herbsSubstance = herbsSubstance.objects.create(
            name=name,
            resumo=descricao,
            oque_e=oque_e,
            beneficios=beneficio,
            boa_para_que=potencial_beneficios,
            doencas_relacionada=doencas_relacionadas,
            desvantagens_cuidados=desvantagens,
            como_funciona=como_funciona,
            dosagem=dosagem,
            faq=faq,
            estudos=estudos_cientificos
        )
        nova_herbsSubstance.save()
        return redirect('herbsSubstances')

    return render(request, 'add_herbsSubstances.html')

def listar_herbsSubstances(request):
    herbsSubstances_items = herbsSubstance.objects.all()

    itens_por_pagina = 7
    paginator = Paginator(herbsSubstances_items, itens_por_pagina)

    # Obtenha o número da página a partir dos parâmetros GET da URL
    page = request.GET.get('page')

    try:
        # Obtenha os itens da página solicitada
        herbsSubstances_items_paginados = paginator.get_page(page)
    except EmptyPage:
        # Caso a página solicitada esteja fora do alcance, retorne a última página
        herbsSubstances_items_paginados = paginator.get_page(paginator.num_pages)

    return render(request, 'list_herbsSubstances.html', {'herbsSubstances_items': herbsSubstances_items_paginados})

def editar_herbsSubstances(request, item_id):
    herbsSubstances_item = get_object_or_404(herbsSubstance, id=item_id)

    if request.method == 'POST':
        # Obtenha os dados atualizados do formulário
        name = request.POST.get('name')
        descricao = request.POST.get('descricao')
        oque_e = request.POST.get('oque_e')
        beneficio = request.POST.get('beneficio')
        potencial_beneficios = request.POST.get('potencial_beneficios')
        doencas_relacionadas = request.POST.get('doencas_relacionadas')
        como_funciona = request.POST.get('como_funciona')
        desvantagens = request.POST.get('desvantagens')
        dosagem = request.POST.get('dosagem')
        faq = request.POST.get('faq')
        estudos_cientificos = request.POST.get('estudos_cientificos')
        # Atualize os campos do objeto herbsSubstances

        herbsSubstances_item.name = name
        herbsSubstances_item.resumo = descricao
        herbsSubstances_item.oque_e = oque_e
        herbsSubstances_item.beneficios = beneficio
        herbsSubstances_item.boa_para_que = potencial_beneficios
        herbsSubstances_item.doencas_relacionada = doencas_relacionadas
        herbsSubstances_item.como_funciona = como_funciona
        herbsSubstances_item.desvantagens_cuidados = desvantagens
        herbsSubstances_item.dosagem = dosagem
        herbsSubstances_item.faq = faq
        herbsSubstances_item.estudos = estudos_cientificos

        # Salve as alterações no banco de dados
        herbsSubstances_item.save()

        return redirect('herbsSubstances')

    return render(request, 'edit_herbsSubstances.html', {'herbsSubstances_item': herbsSubstances_item})




from django.shortcuts import get_object_or_404, redirect
from herbsSubstances.models import herbsSubstance

def excluir_substances(request, item_id):
    if request.method == 'GET':
        # Obter o item a ser excluído
        saude_item = get_object_or_404(herbsSubstance, id=item_id)

        # Excluir o item
        saude_item.delete()

        # Redirecionar para a página de listagem após a exclusão
        return redirect('herbsSubstances')

