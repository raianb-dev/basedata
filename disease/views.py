from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from .models import Doenca

def todos_os_dados(request):
    disease_items = Doenca.objects.all()
    return render(request, 'list_disease.html', {'disease_items': disease_items})

def detalhes_item(request, item_id):
    disease_item = get_object_or_404(Doenca, id=item_id)
    return render(request, 'disease_id.html', {'disease_item': disease_item})

def salvar_disease(request):
    if request.method == 'POST':
        nome_comum = request.POST.get('nome_comum')
        termo_medico = request.POST.get('termo_medico')
        descricao = request.POST.get('descricao')
        causa = request.POST.get('causa')
        prevencao = request.POST.get('prevencao')
        sinal_sintoma = request.POST.get('sinal_sintoma')
        fator_risco = request.POST.get('fator_risco')
        diagnostico_tratamento = request.POST.get('diagnostico_tratamento')
        medidas_gerais = request.POST.get('medidas_gerais')
        medicamentos_gerais = request.POST.get('medicamentos_gerais')
        dieta = request.POST.get('dieta')
        prognostico = request.POST.get('prognostico')
        suplemento = request.POST.get('suplemento')
        faq = request.POST.get('faq')
        referencia = request.POST.get('referencia')

        new_disease = Doenca.objects.create(
            nome_comum=nome_comum,
            termo_medico=termo_medico,
            descricao=descricao,
            causa=causa,
            prevencao=prevencao,
            sinal_sintoma=sinal_sintoma,
            fator_risco=fator_risco,
            diagnostico_tratamento=diagnostico_tratamento,
            medidas_gerais=medidas_gerais,
            medicamentos_gerais=medicamentos_gerais,
            dieta=dieta,
            prognostico=prognostico,
            suplemento=suplemento,
            faq_doença=faq,  # Corrigir o nome do campo aqui para "faq"
            referencia=referencia
        )
  
        return redirect('doenca')

    return render(request, 'add_disease.html')

def listar_disease(request):
    disease_items = Doenca.objects.all()

    # Defina o número de itens por página
    itens_por_pagina = 7
    paginator = Paginator(disease_items, itens_por_pagina)

    # Obtenha o número da página a partir dos parâmetros GET da URL
    page = request.GET.get('page')

    try:
        # Obtenha os itens da página solicitada
        disease_items_paginados = paginator.get_page(page)
    except EmptyPage:
        # Caso a página solicitada esteja fora do alcance, retorne a última página
        disease_items_paginados = paginator.get_page(paginator.num_pages)

    return render(request, 'list_disease.html', {'disease_items': disease_items_paginados})

def editar_disease(request, item_id):
    disease_item = get_object_or_404(Doenca, id=item_id)

    if request.method == 'POST':
        # Obtenha os dados atualizados do formulário
        nome_comum = request.POST.get('nome_comum')
        termo_medico = request.POST.get('termo_medico')
        descricao = request.POST.get('descricao')
        causa = request.POST.get('causa')
        prevencao = request.POST.get('prevencao')
        sinal_sintoma = request.POST.get('sinal_sintoma')
        fator_risco = request.POST.get('fator_risco')
        diagnostico_tratamento = request.POST.get('diagnostico_tratamento')
        medidas_gerais = request.POST.get('medidas_gerais')
        medicamentos_gerais = request.POST.get('medicamentos_gerais')
        dieta = request.POST.get('dieta')
        prognostico = request.POST.get('prognostico')
        suplemento = request.POST.get('suplemento')
        faq_doença = request.POST.get('faq')
        referencia = request.POST.get('estudos_cientificos')

        # Atualize os campos do objeto disease_item
        disease_item.nome_comum = nome_comum
        disease_item.termo_medico = termo_medico
        disease_item.descricao = descricao
        disease_item.causa = causa
        disease_item.prevencao = prevencao
        disease_item.sinal_sintoma = sinal_sintoma
        disease_item.fator_risco = fator_risco
        disease_item.diagnostico_tratamento = diagnostico_tratamento
        disease_item.medidas_gerais = medidas_gerais
        disease_item.medicamentos_gerais = medicamentos_gerais
        disease_item.dieta = dieta
        disease_item.prognostico = prognostico
        disease_item.suplemento = suplemento
        disease_item.faq_doença = faq_doença
        disease_item.referencia = referencia

        # Salve as alterações no banco de dados
        disease_item.save()

        return redirect('doenca')

    return render(request, 'edit_disease.html', {'disease_item': disease_item})

def excluir_disease(request, item_id):
    disease_item = get_object_or_404(Doenca, id=item_id)
    if request.method == 'GET':
        # Verifique se o método da requisição é POST
        # Isso garante que a exclusão ocorra apenas quando o formulário é enviado
        disease_item.delete()
        return redirect('doenca')
    
    # Se a requisição não for POST, renderize o template normalmente
    return render(request, 'list_disease.html', {'disease_items': Doenca.objects.all()})
