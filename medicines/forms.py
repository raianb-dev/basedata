from django import forms
from .models import Medicines

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = ['upload']