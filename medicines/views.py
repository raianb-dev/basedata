from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Medicines, classe_medicamentos, consulta_medicamentos
from .forms import ArquivoForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings

## VIEWS C MEDICAMENTOS ##

def listar_medicamentos(request):
    search_query = request.GET.get('search')
    search_query = search_query if search_query else ""

    if search_query:
        medicamentos = Medicines.objects.filter(
            Q(nome__icontains=search_query) |
            Q(descricao__icontains=search_query) |
            Q(composicao__icontains=search_query) |
            Q(usos__icontains=search_query) |
            Q(contra_indicacoes__icontains=search_query) |
            Q(doencas_situacoes__icontains=search_query) |
            Q(faq__icontains=search_query)
        )
    else:
        medicamentos = Medicines.objects.all()

    itens_por_pagina = 100
    paginator = Paginator(medicamentos, itens_por_pagina)

    page = request.GET.get('page')
    try:
        medicamentos_paginados = paginator.get_page(page)
    except EmptyPage:
        medicamentos_paginados = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        medicamentos_paginados = paginator.get_page(1)

    return render(request, 'list_medicines.html', {'medicamentos': medicamentos_paginados, 
                                                   'search_query': search_query
                                                   })

def adicionar_medicamento(request):
    def get_principios_ativos():
        return consulta_medicamentos.objects.all()
    principio_ativos = get_principios_ativos()
    if request.method == 'POST':
        form_data = request.POST
        uploaded_file = request.FILES.get('upload')

        # Salvar o arquivo no sistema de arquivos
        if uploaded_file:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(uploaded_file.name, uploaded_file)

        principio_ativo = form_data.get('principio_ativo')
        nome_comercial = form_data.get('nome_comercial')
        classe_droga = form_data.get('classe_droga')
        nome_cientifico = form_data.get('nome_cientifico')
        descricao = form_data.get('descricao')
        composicao = form_data.get('composicao_quimica')
        usos = form_data.get('usos_caracteristicas')
        contra_indicacoes = form_data.get('contra_indicacoes')
        doencas_situacoes = form_data.get('doencas_correlacionadas')
        faq = form_data.get('faq')

        medicamento = Medicines.objects.create(
            principio_ativo=principio_ativo,
            nome_comercial=nome_comercial,
            classe_droga=classe_droga,
            nome_cientifico=nome_cientifico,
            descricao=descricao,
            composicao=composicao,
            usos=usos,
            contra_indicacoes=contra_indicacoes,
            doencas_situacoes=doencas_situacoes,
            faq=faq
            
        )
        return redirect('listar_medicamentos')

    return render(request, 'add_medicines.html', {'principios_ativos': principio_ativos})

def editar_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicines, id=medicamento_id)

    if request.method == 'POST':
        form_data = request.POST
        uploaded_file = request.FILES.get('upload')

        # Salvar o novo arquivo no sistema de arquivos, caso tenha sido enviado
        if uploaded_file:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(uploaded_file.name, uploaded_file)
            # Deletar o arquivo antigo associado ao medicamento
            if medicamento.upload:
                fs.delete(medicamento.upload)
            medicamento.upload = filename

        medicamento.principio_ativo = form_data.get('principio_ativo')
        medicamento.nome_comercial = form_data.get('nome_comercial')
        medicamento.classe_droga = form_data.get('classe_droga')
        medicamento.nome_cientifico = form_data.get('nome_cientifico')
        medicamento.descricao = form_data.get('descricao')
        medicamento.composicao = form_data.get('composicao_quimica')
        medicamento.usos = form_data.get('usos_caracteristicas')
        medicamento.contra_indicacoes = form_data.get('contra_indicacoes')
        medicamento.doencas_situacoes = form_data.get('doencas_correlacionadas')
        medicamento.faq = form_data.get('faq')

        medicamento.save()

        return redirect('listar_medicamentos')

    return render(request, 'edit_medicines.html', {'medicamento': medicamento})

def excluir_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicines, id=medicamento_id)

    if request.method == 'GET':
        medicamento.delete()
        return redirect('listar_medicamentos')

    return render(request, 'list_medicines.html', {'medicamentos': Medicines.objects.all()})
from django.core import serializers
from django.http import JsonResponse
def get_product_names(request):
    selected_main_active = request.GET.get('selected_main_active')
    products = consulta_medicamentos.objects.filter(main_active=selected_main_active)
    products_data = serializers.serialize('json', products, fields=('id', 'product_name'))
    return JsonResponse(products_data, safe=False)



def adicionar_cosulta(request):
    if request.method == 'POST':
        form_data = request.POST

        name_product = form_data.get('name_product')
        main_active = form_data.get('main_active')
        register = form_data.get('register')
        process = form_data.get('proccess')
        cnpj = form_data.get('cnpj')
        situation = form_data.get('situation')
        maturity = form_data.get('vencimento')

        consulta = consulta_medicamentos.objects.create(
            product_name = name_product,
            main_active = main_active,
            register = register,
            preccess = process,
            cpnj = cnpj,
            situation = situation,
            maturity = maturity
        )
        consulta.save()
        return redirect('listar_medicamentos')
    return render(request,'add_consulta.html')

def excluir_consulta(request, consulta_id):
    consulta = get_object_or_404(consulta_medicamentos, id=consulta_id)
    if request.method == 'GET':
        consulta_medicamentos.delete()
        return redirect('listar_medicamentos')


## VIEWS CLASSE DE DROGAS ##

def listar_classe(request):
    classe = classe_medicamentos.objects.all()
    return render(request, 'list_classe.html', {'classe': classe})

def adicionar_classe(request):
    if request.method == 'POST':
        form_data = request.POST
        name = form_data.get('name')
        classe = classe_medicamentos.objects.create(
            name=name
        )
        return redirect(request, 'listar_medicamentos')
    return render('list_medicines.html')

def excluir_classe(request, classe_id):
    if request.method == 'GET':
        search = get_object_or_404(classe_medicamentos, id=classe_id)
        classe_medicamentos.delete()
        return redirect(request, 'listar_medicamentos')