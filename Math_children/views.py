from django.http import HttpResponse
from django.template import Template, Context
from django.urls import reverse_lazy
from Math_children.models import Usuario    
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import formularioUsuario

def Index(request):
    archivobase = open("Math_children\Templates\Index.html")
    lectura = Template(archivobase.read())
    archivobase.close()
    parametros = Context()
    paginaresultado = lectura.render(parametros)
    return HttpResponse(paginaresultado)

def Download(request):
    archivobase = open("Math_children\Templates\Download.html")
    lectura = Template(archivobase.read())
    archivobase.close()
    parametros = Context()
    paginaresultado = lectura.render(parametros)
    return HttpResponse(paginaresultado)

def Insertar_usuario(request):
    if request.method=="POST":
         if request.POST.get('nombre_usu') and request.POST.get('apellidos_usu') and request.POST.get('documento_usu') and request.POST.get('email_usu') and request.POST.get('contrase_usu')and request.POST.get('nombre'):
            usuario = User.objects.create_user(
            username=request.POST.get('nombre_usu'),  # Usa email_usu como el username
            email=request.POST.get('email_usu'),
            password=request.POST.get('contrase_usu'),
            first_name = request.POST.get('nombre'),
            last_name = request.POST.get('apellidos_usu'),
            documento_usu = request.POST.get('documento_usu')
            )
            usuario.save()
            # insertar.execute("call Insertar_usuario('"+usuarios.nombre_usu+"','"+usuarios.apellidos_usu+"','"+usuarios.documento_usu+"','"+usuarios.email_usu+"','"+usuarios.contrase_usu+"')")
            return redirect('Ingreso')

    else:
        return render (request,'Register.html')
    
def Ingreso(request):
    if request.method == "POST":
        if request.POST.get('nombre_usu') and request.POST.get('contrase_usu'):
            user = authenticate(username=request.POST.get('nombre_usu'), password=request.POST.get('contrase_usu'))
            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logueado como ")
                return redirect("/ListadoUsuario/")
            else:
                mensaje ="Correo o contraseña incorrectos"
                return render(request, 'Login.html', {'mensaje':mensaje})
    else:
        return render(request, 'Login.html')
        
def Logout(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("/Index/")

# @login_required
def VistaUsuario(request):
    usuario = User.objects.all()
    archivobase = open("Math_children\Templates\VistaUsu.html")
    lectura = Template(archivobase.read())
    archivobase.close()
    parametros = Context({'usuario':usuario})
    paginaresultado = lectura.render(parametros)
    return HttpResponse(paginaresultado)
#Vista basadas en clases
class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'VistaUsu.html'
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo = True)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = formularioUsuario
    template_name = 'Register.html'
    success_url = reverse_lazy('Ingreso')