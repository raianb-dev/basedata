from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Doenca

def todos_os_dados(request):
    disease_items = Doenca.objects.all()
    return render(request, 'list_disease.html', {'disease_items': disease_items})

def detalhes_item(request, item_id):
    disease_item = get_object_or_404(Doenca, id=item_id)
    return render(request, 'disease_id.html', {'disease_item': disease_item})

def salvar_disease(request):
    if request.method == 'POST':
        # Get data from the form
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
        faq_doenca = request.POST.get('faq')
        referencia = request.POST.get('referencia')

        # Create a new Doenca object with the received data
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
            faq_doenca=faq_doenca,
            referencia=referencia
        )
  
        return redirect('doenca')

    return render(request, 'add_disease.html')

def listar_disease(request):
    search_query = request.GET.get('search')
    
    # Check if the value of search_query is None and replace it with an empty string
    search_query = search_query if search_query else ""

    if search_query:
        # Use the Q object to combine filters and get a more refined search
        disease_items = Doenca.objects.filter(
            Q(nome_comum__icontains=search_query) |
            Q(termo_medico__icontains=search_query) |
            Q(descricao__icontains=search_query) |
            Q(causa__icontains=search_query) |
            Q(prevencao__icontains=search_query) |
            Q(sinal_sintoma__icontains=search_query) |
            Q(fator_risco__icontains=search_query) |
            Q(diagnostico_tratamento__icontains=search_query) |
            Q(medidas_gerais__icontains=search_query) |
            Q(medicamentos_gerais__icontains=search_query) |
            Q(dieta__icontains=search_query) |
            Q(prognostico__icontains=search_query) |
            Q(suplemento__icontains=search_query) |
            Q(faq_doenca__icontains=search_query) |
            Q(referencia__icontains=search_query)
        )
    else:
        disease_items = Doenca.objects.all()

    # Paginate the results
    itens_por_pagina = 3
    paginator = Paginator(disease_items, itens_por_pagina)

    page = request.GET.get('page')
    try:
        disease_items_paginados = paginator.get_page(page)
    except EmptyPage:
        # If the requested page is out of range, return the last page
        disease_items_paginados = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        # If the page number is not an integer, show the first page
        disease_items_paginados = paginator.get_page(1)

    return render(request, 'list_disease.html', {'disease_items': disease_items_paginados, 'search_query': search_query})


def editar_disease(request, item_id):
    disease_item = get_object_or_404(Doenca, id=item_id)

    if request.method == 'POST':
        # Get updated data from the form
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
        faq_doenca = request.POST.get('faq')
        referencia = request.POST.get('referencia')

        # Update the fields of the disease_item object
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
        disease_item.faq_doenca = faq_doenca
        disease_item.referencia = referencia

        # Save the changes to the database
        disease_item.save()

        return redirect('doenca')

    return render(request, 'edit_disease.html', {'disease_item': disease_item})

def excluir_disease(request, item_id):
    disease_item = get_object_or_404(Doenca, id=item_id)
    if request.method == 'GET':
        # Check if the request method is POST
        # This ensures that the deletion occurs only when the form is submitted
        disease_item.delete()
        return redirect('doenca')
    
    # If the request is not POST, render the template normally
    return render(request, 'list_disease.html', {'disease_items': Doenca.objects.all()})
