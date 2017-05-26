from django.shortcuts import render,redirect
from modules.users.forms import UserForm
from modules.modulo_cuatro.forms import LoginForm
from modules.foro.forms import ComentarioForm, RespuestaForm
from modules.foro.models import Comentario, Respuesta
from modules.users.models import User
from django.contrib.auth import authenticate,logout as salir,login as iniciar
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="modulo_cuatro:login")
def index(request):
    if request.user.is_authenticated():
        print(request.user.id)
    return render(request,'modulo_cuatro/index.html')

@login_required(login_url="modulo_cuatro:login")
def registro(request):
    if not request.user.nombre:  
        form = UserForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                u = request.user
                u.nombre = request.POST['nombre']
                u.apellido_paterno = request.POST['apellido_paterno']
                u.apellido_materno = request.POST['apellido_materno']
                u.telefono = request.POST['telefono']
                u.sexo = request.POST['sexo']
                u.save()
                return redirect('modulo_cuatro:exito')
    else:
        return redirect('modulo_cuatro:exito')
    return render(request,'modulo_cuatro/registro.html',{'form':form})

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                iniciar(request,user)
                return redirect('modulo_cuatro:index')
            else:
                return HttpResponse("Usuario no encontrado")

    return render(request,'modulo_cuatro/login.html', {"login":form})

def logout(request):
    salir(request)
    return redirect("landing:index")

@login_required(login_url="modulo_cuatro:login")
def foro(request):
    form_comentario = ComentarioForm(request.POST or None)
    form_respuesta = RespuestaForm(request.POST or None)

    c = Comentario.objects.all().select_related()

    r = Respuesta.objects.all().select_related()

    return render(request,'modulo_cuatro/foro.html',
    {
        'form_comentario':form_comentario,
        'form_respuesta':form_respuesta,
        'comentarios':c,
        'respuestas':r,
    }
    )


@login_required(login_url="modulo_cuatro:login")
def add_comentario(request):
    if request.method == 'POST':
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            Comentario = form_comentario.save(commit=False)
            u = request.user
            Comentario.user = u
            Comentario.save()
            return redirect('modulo_cuatro:foro')


@login_required(login_url="modulo_cuatro:login")            
def add_respuesta(request):
    if request.method == 'POST':
        form_respuesta = RespuestaForm(request.POST)
        if form_respuesta.is_valid():
            Respuesta = form_respuesta.save(commit=False)
            c = Comentario.objects.get(id=int(request.POST['comentario_id']))
            u = request.user
            Respuesta.comentario = c
            Respuesta.user = u
            Respuesta.save()
            return redirect('modulo_cuatro:foro')

def exito(request):
    return render(request,'modulo_cuatro/exito.html')