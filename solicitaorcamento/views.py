from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from solicitaorcamento.forms import OrcForm


def formulario(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            data = {}
            data['formulario'] = OrcForm()
            return render(request, 'orcamentoform.html', data)
        else:
            return render(request, 'logar.html')


def create(request):
    form = OrcForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'success.html')

#-------------------------------------------------------------
#English

def formularioen(request):
    data = {}
    data['formularioen'] = OrcForm()
    return render(request, 'orcamentoformen.html', data)