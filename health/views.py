from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Saude

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
        name = request.POST.get('name')
        descricao = request.POST.get('descricao')
        mecanismo = request.POST.get('mecanismo')
        beneficio = request.POST.get('beneficio')
        efeitos_colaterais = request.POST.get('efeitos_colaterais')
        interacoes = request.POST.get('interacoes')
        experiencia = request.POST.get('experiencia')
        estudos_cientificos = request.POST.get('estudos_cientificos')
        faq = request.POST.get('faq')

        saude = Saude.objects.create(
            name=name,
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
    itens_por_pagina = 100
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
        name = request.POST.get('name')
        description = request.POST.get('description')
        mecanismo = request.POST.get('action_mechanisms')
        beneficio = request.POST.get('potential_benefits')
        efeitos_colaterais = request.POST.get('effects_precautions')
        interacoes = request.POST.get('gene_interactions')
        experiencia = request.POST.get('user_experience')
        estudos_cientificos = request.POST.get('scientific_studies')
        faq = request.POST.get('faq')

        # Atualize os campos do objeto Saude
        saude_item.name = name
        saude_item.description = description
        saude_item.action_mechanisms = mecanismo
        saude_item.potential_benefits = beneficio
        saude_item.effects_precautions = efeitos_colaterais
        saude_item.gene_interactions = interacoes
        saude_item.user_experience = experiencia
        saude_item.scientific_studies = estudos_cientificos
        saude_item.faq = faq

        # Salve as alterações no banco de dados
        saude_item.save()

        return redirect('health')

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


def listar_saude(request):
    search_query = request.GET.get('search')
    
    # Verifique se o valor de search_query é None e substitua por uma string vazia
    search_query = search_query if search_query else ""

    if search_query:
        # Use o Q object para combinar filtros e obter uma pesquisa mais refinada
        saude_items = Saude.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(action_mechanisms__icontains=search_query) |
            Q(potential_benefits__icontains=search_query) |
            Q(effects_precautions__icontains=search_query) |
            Q(gene_interactions__icontains=search_query) |
            Q(scientific_studies__icontains=search_query) |
            Q(user_experience__icontains=search_query) |
            Q(faq__icontains=search_query)
        )
    else:
        saude_items = Saude.objects.all()

    # Paginar os resultados
    itens_por_pagina = 100
    paginator = Paginator(saude_items, itens_por_pagina)

    page = request.GET.get('page')
    try:
        saude_items_paginados = paginator.get_page(page)
    except EmptyPage:
        # Se a página solicitada estiver fora do alcance, exibir a última página
        saude_items_paginados = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        # Se o número da página não for um inteiro, exibir a primeira página
        saude_items_paginados = paginator.get_page(1)

    return render(request, 'list_saude.html', {'saude_items': saude_items_paginados, 'search_query': search_query})

