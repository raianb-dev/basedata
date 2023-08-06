from django.contrib import admin
from django.urls import path

# Importações locais #
from health import views as views_health
from herbsSubstances import views as views_herbsSubstances
from disease import views as views_disease
from home import views as views_home
from medicines import views as views_medicines 
# Urls "admin"
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Urls "saude"
urlpatterns = [

    # Routes "saude"
    path('saude/', views_health.listar_saude, name='health'),
    path('saude/cadastrar/', views_health.salvar_saude, name='add-saude'),
    path('saude/editar/<int:item_id>/', views_health.editar_saude, name='editar-saude'),
    path('saude/excluir/<int:item_id>/', views_health.excluir_saude, name='excluir-saude'),

    # Routes "herbs"
    path('ervas/', views_herbsSubstances.listar_herbsSubstances, name='herbsSubstances'),
    path('ervas/cadastrar/', views_herbsSubstances.salvar_herbsSubstances, name='add-herbsSubstances'),
    path('ervas/editar/<int:item_id>/', views_herbsSubstances.editar_herbsSubstances, name='editar-herbsSubstances'),
    path('ervas/excluir/<int:item_id>/', views_herbsSubstances.excluir_substances, name='excluir-herbsSubstances'),
    # Routes "Doença"
    path('doenca/', views_disease.listar_disease, name='doenca'),
    path('doenca/<int:item_id>/', views_disease.detalhes_item, name='doenca-id'),
    path('doenca/cadastrar', views_disease.salvar_disease, name='add-doenca'),
    path('doenca/editar/<int:item_id>/', views_disease.editar_disease, name='editar-doenca'),
    path('doenca/excluir/<int:item_id>/', views_disease.excluir_disease, name='excluir-doenca'),

    # Routes "medicamentos"
    path('medicamentos/', views_medicines.listar_medicamentos, name='listar_medicamentos'),
    path('medicamentos/cadastrar/', views_medicines.adicionar_medicamento, name='adicionar_medicamento'),
    path('medicamentos/editar/<int:medicamento_id>/', views_medicines.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/excluir/<int:medicamento_id>/', views_medicines.excluir_medicamento, name='excluir_medicamento'),

    # Routes "Consultar_medicamentos"
    path('consulta_medicamento/cadastrar', views_medicines.adicionar_cosulta, name='adicionar_consulta'),
    path('consulta_medicamento/excluir/<int:item_id>/',views_medicines.excluir_consulta, name='excluir_consulta'),

    # Routes "classe_medicamento"
    path('classe/', views_medicines.listar_classe, name='listar_classe'),
    path('classe/cadastrar', views_medicines.adicionar_classe, name='adicionar_classe'),
    path('classe/excluir/<int:item_id>/',views_medicines.excluir_classe, name='exluir_classe'),

    # product name # 
    path('get_product_names/', views_medicines.get_product_names, name='get_product_names'),

    # Routes "home"
    path('', views_home.redirect, name='home'),
]
