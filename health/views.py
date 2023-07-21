from django.shortcuts import render, get_object_or_404, redirect
from health import models
Saude = models.Saude
from .forms import SaudeForm

def todos_os_dados(request):
    saude_items = Saude.objects.all()
    return render(request, 'saude.html', {'saude_items': saude_items})

def detalhes_item(request, item_id):
    saude_item = get_object_or_404(Saude, id=item_id)
    return render(request, 'saude_id.html', {'saude_item': saude_item})
    
def cadastrar_saude(request):
    if request.method == 'POST':
        form = SaudeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('health')
    else:
        form = SaudeForm()

    return render(request, 'add_saude.html', {'form': form})

