"""
Historial de Modificaciones:
Fecha       Autor  Proyecto    Descripción
05/06/2017  ASR    diplomado   
"""
from django.shortcuts import render,redirect
from modules.users.forms import UserForm
from modules.modulo_cuatro.forms import LoginForm
from modules.foro.forms import ComentarioForm, RespuestaForm
from modules.archivos.forms import ArchivoForm
from modules.foro.models import Comentario, Respuesta
from modules.users.models import User
from modules.etapas.models import Etapa
from modules.archivos.models import Archivo
from modules.modulo_cuatro.models import ModuloCuatro
from django.contrib.auth import authenticate,logout as salir,login as iniciar
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.http import Http404
from django.http import HttpResponse
# Create your views here.
def modulo_cuatro_actualiza(usuario,etapa):
    lista_modulo_cuatro = ModuloCuatro.objects.filter(user__id=usuario.id)
    lista_etapas = Etapa.objects.all()
    print(len(lista_modulo_cuatro))
    if len(lista_modulo_cuatro) == 0:
        for le in lista_etapas:
            if le.id == etapa:
                mc = ModuloCuatro.objects.create(user=usuario,etapa=le,activo=True)
            else:
                mc = ModuloCuatro.objects.create(user=usuario,etapa=le,activo=False)        
    else:
        mc = ModuloCuatro.objects.get(user__id=usuario.id,etapa__id=etapa)
        print(mc)
        mc.activo = True
        mc.save()

@login_required(login_url="modulo_cuatro:login")        
def add_archivo(request):
    u = request.user
    try:
        a = Archivo.objects.get(etapa__id=4,user__id=u.id)
    except Archivo.DoesNotExist:
        a = None

    if a is None:
        if request.method == "POST":
            form_archivo = ArchivoForm(request.POST,request.FILES)
            if form_archivo.is_valid():
                
                documento = form_archivo.save(commit=False)
                documento.user = u
                e = Etapa.objects.get(id=request.POST['etapa_id'])
                documento.etapa = e
                documento.save()
                modulo_cuatro_actualiza(u,request.POST['etapa_id'])
                return redirect('modulo_cuatro:exito')
    else:
        return redirect('modulo_cuatro:exito')
   
@login_required(login_url="modulo_cuatro:login")
def segunda_etapa(request):
    u = request.user
    
    try:
        a = Archivo.objects.get(etapa__id=4,user__id=u.id)
    except Archivo.DoesNotExist:
        a = None
    
    print(a)
    if a is None:
        form_archivo = ArchivoForm(request.POST or None)
        return render(request,'modulo_cuatro/segunda_etapa.html',
        {
            'form_archivo':form_archivo,
        }
        )
    else:
        return redirect('modulo_cuatro:exito')

def proyecto_final(request):
    u = request.user
    
    try:
        a = Archivo.objects.get(etapa__id=7,user__id=u.id)
    except Archivo.DoesNotExist:
        a = None
    
    print(a)
    if a is None:
        form_archivo = ArchivoForm(request.POST or None)
        return render(request,'modulo_cuatro/proyecto_final.html',
        {
            'form_archivo':form_archivo,
        }
        )
    else:
        return redirect('modulo_cuatro:exito')
        

    
    
    

@login_required(login_url="modulo_cuatro:login")
def index(request):
    if request.user.is_authenticated():
        u = request.user
        modulo_cuatro_actualiza(u,1)
        print(request.user.id)
    return render(request,'modulo_cuatro/index.html')



@login_required(login_url="modulo_cuatro:login")
def registro(request):
    if not request.user.nombre: 
        form = UserForm(request.POST or None)
        return render(request,'modulo_cuatro/registro.html',{'form':form})
    else:
        return redirect('modulo_cuatro:exito')
    
@login_required(login_url="modulo_cuatro:login")
def update_user(request):
    if not request.user.nombre:  
        form = UserForm(request.POST or None)        
        if request.method == 'POST':
            if form.is_valid():
                u = request.user
                u.nombre = request.POST['nombre']
                u.apellido_paterno = request.POST['apellido_paterno']
                u.apellido_materno = request.POST['apellido_materno']
                u.telefono = request.POST['telefono']
                #u.sexo = request.POST['sexo']
                u.save()
                modulo_cuatro_actualiza(u,2)
                modulo_cuatro_actualiza(u,3)  
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

@login_required(login_url="modulo_cuatro:login")
def exito(request):
    return render(request,'modulo_cuatro/exito.html')