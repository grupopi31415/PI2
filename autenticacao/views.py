from django.shortcuts import render, redirect
from django.http import HttpResponse
from solicitaorcamento.views import formulario
from users.models import Usuario

from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('formulario')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        form = Usuario(request.POST or None)

        nome = request.POST.get('nome')
        sobrenome = request.POST.get('lastname')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('num')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        celular = request.POST.get('tel')
        email = request.POST.get('email')
        username = request.POST.get('usuario')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmepassword')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')

        if len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect ('/auth/cadastro')

        usuario = Usuario.objects.filter(username = username)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
            return redirect('/auth/cadastro')

        try:

            usuario = Usuario.objects.create_user(first_name=nome, last_name=sobrenome, cep=cep, endereco=endereco, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, estado=estado, celular=celular, username=username, email=email, password=senha)
            usuario.save()

            return redirect('/auth/logar')

        except:

            return redirect('/auth/cadastro')


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('formulario')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=senha)
    if not usuario:
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return redirect('/auth/logar')
    else:
        auth.login(request, usuario)
        return redirect('formulario')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')


#-----------------------------------------------------------------------
#English

def logaren(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('formularioen')
        return render(request, 'logaren.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=senha)
    if not usuario:
        messages.add_message(request, constants.ERROR, 'Username or password wrong')
        return redirect('/auth/logaren')
    else:
        auth.login(request, usuario)
        return redirect('formularioen')

def cadastroen(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('formularioen')
        return render(request, 'cadastroen.html')
    elif request.method == "POST":
        form = Usuario(request.POST or None)
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('lastname')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('num')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        celular = request.POST.get('tel')
        email = request.POST.get('email')
        username = request.POST.get('usuario')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmepassword')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "Passwords don't match")
            return redirect('/auth/cadastroen')

        if len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Fill in all fields')
            return redirect('/auth/cadastroen')

        usuario = Usuario.objects.filter(username=username)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'User already exists')
            return redirect('/auth/cadastroen')

        try:

            usuario = Usuario.objects.create_user(first_name=nome, last_name=sobrenome, cep=cep, endereco=endereco,
                                                  numero=numero, complemento=complemento, bairro=bairro,
                                                  cidade=cidade, estado=estado, celular=celular, username=username,
                                                  email=email, password=senha)
            usuario.save()

            return redirect('/auth/logaren')

        except:

            return redirect('/auth/cadastroen')


def sairen(request):
    auth.logout(request)
    return redirect('/auth/logaren')