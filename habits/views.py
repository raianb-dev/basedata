from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Habits
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def listar_habits(request):
    search_query = request.GET.get('search')

    # Verifique se o valor de search_query é None e substitua por uma string vazia
    search_query = search_query if search_query else ""

    if search_query:
        # Use o Q object para combinar filtros e obter uma pesquisa mais refinada
        habits_items = Habits.objects.filter(
            Q(nome__icontains=search_query) |
            Q(equipamentos_requisitos__icontains=search_query) | 
            Q(action_mechanisms__icontains=search_query) |
            Q(como_fazer__icontains=search_query) |
            Q(por_que_funciona__icontains=search_query) |
            Q(tempo_estimado__icontains=search_query) |
            Q(frequencia__icontains=search_query) |
            Q(hora_do_dia__icontains=search_query) |
            Q(efeitos=search_query) |
            Q(dicas_icontains=search_query) ) 
    else:
        habits_items = Habits.objects.all()

    # Paginar os resultados
    itens_por_pagina = 100
    paginator = Paginator(habits_items, itens_por_pagina)

    page = request.GET.get('page')
    try:
        habits_items_paginados = paginator.get_page(page)
    except EmptyPage:
        # Se a página solicitada estiver fora do alcance, exibir a última página
        habits_items_paginados = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        # Se o número da página não for um inteiro, exibir a primeira página
        habits_items_paginados = paginator.get_page(1)

    return render(request, 'list_habits.html', {
        'habits_items': habits_items_paginados,
        'search_query': search_query
    })


def salvar_habits(request):
    if request.method == 'POST':
        form_data = request.POST

        nome = form_data.get('nome'),
        descricao = form_data.get('descricao'),
        equipamentos_requisitos = form_data.get('equipamentos_requisitos'),
        como_fazer = form_data.get('como_fazer'),
        por_que_funciona = form_data.get('por_que_funciona'),
        tempo_estimado = form_data.get('tempo_estimado'),
        frequencia = form_data.get('frequencia'),
        hora_do_dia = form_data.get('hora_do_dia'),
        efeitos = form_data.get('efeitos'),
        dicas = form_data.get('dicas')

        new = Habits.objects.create(
            nome = nome,
            descricao = descricao,
            equipamentos_requisitos = equipamentos_requisitos,
            como_fazer = como_fazer,
            por_que_funciona = por_que_funciona,
            tempo_estimado = tempo_estimado,
            frequencia = frequencia,
            hora_do_dia = hora_do_dia,
            efeitos = efeitos,
            dicas = dicas
        )
        new.save()
        print(new)
        return redirect('habits')
    return render(request, 'add_habits.html')


def editar_habits(request):
    pass


def excluir_habits(request, item_id):
    saude_item = get_object_or_404(Habits, id=item_id)
    if request.method == 'GET':
        # Verifique se o método da requisição é POST
        # Isso garante que a exclusão ocorra apenas quando o formulário é enviado
        saude_item.delete()
        return redirect('habits')
    
    # Se a requisição não for POST, renderize o template normalmente
    return render(request, 'list_habits.html', {'habits_items': Habits.objects.all()})