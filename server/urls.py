
from django.contrib import admin
from django.urls import path

# Importações locais #
from health import views as views_health
from disease import views as views_disease
from home import views as views_home

# Urls "admin"
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Urls "saude"
urlpatterns = [
    path('saude/', views_health.todos_os_dados, name='health'),
    path('saude/<int:id>/', views_health.detalhes_item, name='health-id'),
    path('saude/cadastrar/', views_health.cadastrar_saude, name='add-saude'),
    path('doenca/', views_disease.todos_os_dados, name='disease'),
    path('doenca/<int:id>/', views_disease.detalhes_item, name='disease-id'),
    path('home/', views_home.redirect, name='home'),

]
