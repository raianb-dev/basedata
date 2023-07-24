from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage

from health import models
Saude = models.Saude


def todos_os_dados(request):
    saude_items = Saude.objects.all()
    return render(request, 'list_saude.html', {'saude_items': saude_items})

def detalhes_item(request, item_id):
    saude_item = get_object_or_404(Saude, id=item_id)
    return render(request, 'saude_id.html', {'saude_item': saude_item})
    
def salvar_saude(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        mecanismo = request.POST.get('mecanismo')
        beneficio = request.POST.get('beneficio')
        efeitos_colaterais = request.POST.get('efeitos_colaterais')
        interacoes = request.POST.get('interacoes')
        experiencia = request.POST.get('experiencia')
        estudos_cientificos = request.POST.get('estudos_cientificos')
        faq = request.POST.get('faq')

        saude = Saude.objects.create(
            description=descricao,
            action_mechanisms=mecanismo,
            potential_benefits=beneficio,
            effects_precautions=efeitos_colaterais,
            gene_interactions=interacoes,
            user_experience=experiencia,
            scientific_studies=estudos_cientificos,
            faq=faq
        )
        return redirect('health')

    return render(request, 'add_saude.html')

def listar_saude(request):
    saude_items = Saude.objects.all()

    # Defina o número de itens por página
    itens_por_pagina = 7
    paginator = Paginator(saude_items, itens_por_pagina)

    # Obtenha o número da página a partir dos parâmetros GET da URL
    page = request.GET.get('page')

    try:
        # Obtenha os itens da página solicitada
        saude_items_paginados = paginator.get_page(page)
    except EmptyPage:
        # Caso a página solicitada esteja fora do alcance, retorne a última página
        saude_items_paginados = paginator.get_page(paginator.num_pages)

    return render(request, 'list_saude.html', {'saude_items': saude_items_paginados})

def editar_saude(request, item_id):
    saude_item = get_object_or_404(Saude, id=item_id)

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

        # Atualize os campos do objeto Saude
        saude_item.description = descricao
        saude_item.action_mechanisms = mecanismo
        saude_item.potential_benefits = beneficio
        saude_item.effects_precautions = efeitos_colaterais
        saude_item.gene_interactions = interacoes
        saude_item.user_experience = experiencia
        saude_item.scientific_studies = estudos_cientificos
        saude_item.faq = faq

        # Salve as alterações no banco de dados
        saude_item.save()

        return redirect('listar-saude')

    return render(request, 'edit_saude.html', {'saude_item': saude_item})


def excluir_saude(request, item_id):
    saude_item = get_object_or_404(Saude, id=item_id)
    if request.method == 'GET':
        # Verifique se o método da requisição é POST
        # Isso garante que a exclusão ocorra apenas quando o formulário é enviado
        saude_item.delete()
        return redirect('health')
    
    # Se a requisição não for POST, renderize o template normalmente
    return render(request, 'list_saude.html', {'saude_items': Saude.objects.all()})