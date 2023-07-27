from django.contrib import admin
from django.urls import path

# Importações locais #
from health import views as views_health
from herbsSubstances import views as views_herbsSubstances
from disease import views as views_disease
from home import views as views_home

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
    path('ervas/', views_herbsSubstances.todos_os_dados, name='herbsSubstances'),
    path('ervas/cadastrar/', views_herbsSubstances.salvar_herbsSubstances, name='add-herbsSubstances'),
    path('ervas/editar/<int:item_id>/', views_herbsSubstances.editar_herbsSubstances, name='editar-herbsSubstances'),
    path('ervas/excluir/<int:item_id>/', views_herbsSubstances.excluir_herbsSubstances, name='excluir-herbsSubstances'),
    # Routes "Doença"
    path('doenca/', views_disease.listar_disease, name='doenca'),
    path('doenca/<int:item_id>/', views_disease.detalhes_item, name='doenca-id'),
    path('doenca/cadastrar', views_disease.salvar_disease, name='add-doenca'),
    path('doenca/editar/<int:item_id>/', views_disease.editar_disease, name='editar-doenca'),
    path('doenca/excluir/<int:item_id>/', views_disease.excluir_disease, name='excluir-doenca'),

    # Routes "home"
    path('', views_home.redirect, name='home'),
]
