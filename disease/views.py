from django.shortcuts import render, get_object_or_404
from disease import models
doenca = models.Doenca

def todos_os_dados(request):
    doenca_items = doenca.objects.all()
    return render(request, 'doenca.html', {'doenca_items': doenca_items})

def detalhes_item(request, item_id):
    doenca_item = get_object_or_404(doenca, id=item_id)
    return render(request, 'doenca_id.html', {'doenca_item': doenca_item})
