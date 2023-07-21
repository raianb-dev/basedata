from django import forms
from .models import Saude

class SaudeForm(forms.ModelForm):
    class Meta:
        model = Saude
        fields = '__all__'  # Você pode especificar os campos desejados aqui, ou '__all__' para todos os campos do modelo
