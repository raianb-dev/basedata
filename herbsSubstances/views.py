from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage

from herbsSubstances import models
herbsSubstances = models.herbsSubstance


def todos_os_dados(request):
    herbsSubstances_items = herbsSubstances.objects.all()
    return render(request, 'list_herbsSubstances.html', {'herbsSubstances_items': herbsSubstances_items})

def detalhes_item(request, item_id):
    herbsSubstances_item = get_object_or_404(herbsSubstances, id=item_id)
    return render(request, 'herbsSubstances_id.html', {'herbsSubstances_item': herbsSubstances_item})
    
def salvar_herbsSubstances(request):
    if request.method == 'POST':
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
        nova_herbsSubstance = herbsSubstances.objects.create(
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
    herbsSubstances_items = herbsSubstances.objects.all()

    # Defina o número de itens por página
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
    herbsSubstances_item = get_object_or_404(herbsSubstances, id=item_id)

    if request.method == 'POST':
        # Obtenha os dados atualizados do formulário
        descricao = request.POST.get('descricao')
        mecanismo = request.POST.get('mecanismo')
        beneficio = request.POST.get('beneficio')
        efeitos_colaterais = request.POST.get('efeitos_colaterais')
        interacoes = request.POST.get('interacoes')
        experiencia = request.POST.get('experiencia')
        estudos_cientificos = request.POST.get('estudos_cientificos')
        faq = request.POST.get('faq')

        # Atualize os campos do objeto herbsSubstances
        herbsSubstances_item.description = descricao
        herbsSubstances_item.action_mechanisms = mecanismo
        herbsSubstances_item.potential_benefits = beneficio
        herbsSubstances_item.effects_precautions = efeitos_colaterais
        herbsSubstances_item.gene_interactions = interacoes
        herbsSubstances_item.user_experience = experiencia
        herbsSubstances_item.scientific_studies = estudos_cientificos
        herbsSubstances_item.faq = faq

        # Salve as alterações no banco de dados
        herbsSubstances_item.save()

        return redirect('listar-herbsSubstances')

    return render(request, 'edit_herbsSubstances.html', {'herbsSubstances_item': herbsSubstances_item})


def excluir_herbsSubstances(request, item_id):
    herbsSubstances_item = get_object_or_404(herbsSubstances, id=item_id)
    if request.method == 'GET':
        # Verifique se o método da requisição é POST
        # Isso garante que a exclusão ocorra apenas quando o formulário é enviado
        herbsSubstances_item.delete()
        return redirect('herbsSubstances')
    
    # Se a requisição não for POST, renderize o template normalmente
    return render(request, 'list_herbsSubstances.html', {'herbsSubstances_items': herbsSubstances.objects.all()})