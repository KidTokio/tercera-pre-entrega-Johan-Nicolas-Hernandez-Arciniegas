from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def verClientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "cliente.html", contexto) 

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            clienteNombre = miForm.cleaned_data.get("nombre")
            clienteApellido = miForm.cleaned_data.get("apellido")
            clienteEmail = miForm.cleaned_data.get("email")
            clienteNumero = miForm.cleaned_data.get("numero")
            clienteDireccion = miForm.cleaned_data.get("direccion")
            cliente = Cliente(nombre=clienteNombre, apellido=clienteApellido, email=clienteEmail, numero=clienteNumero, direccion=clienteDireccion)
            cliente.save()
            contexto = {'clientes': Cliente.objects.all()}
            return render(request, "clienteSucces.html", contexto)
    
    else:
        miForm = ClienteForm()
    
    return render(request, "clienteForm.html", {"form": miForm})

def verUsuarios(request):
    contexto = {'usuarios': Usuario.objects.all()}
    return render(request, "usuario.html", contexto) 

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuarioNombre = miForm.cleaned_data.get("nombre")
            usuarioApellido = miForm.cleaned_data.get("apellido")
            usuarioEmail = miForm.cleaned_data.get("email")
            usuarioNumero = miForm.cleaned_data.get("numero")
            usuarioDireccion = miForm.cleaned_data.get("direccion")
            usuarioClave = miForm.cleaned_data.get("clave")
            usuario = Usuario(nombre=usuarioNombre, apellido=usuarioApellido, email=usuarioEmail, numero=usuarioNumero, direccion=usuarioDireccion, clave=usuarioClave)
            usuario.save()
            contexto = {'usuarios': Usuario.objects.all()}
            return render(request, "usuarioSucces.html", contexto)
    
    else:
        miForm = UsuarioForm()
    
    return render(request, "usuarioForm.html", {"form": miForm})

def verArticulos(request):
    contexto = {'articulos': Articulo.objects.all()}
    return render(request, "articulo.html", contexto) 

def articuloForm(request):
    if request.method == "POST":
        miForm = ArticuloForm(request.POST)
        if miForm.is_valid():
            articuloNombre = miForm.cleaned_data.get("nombre")
            articuloCategoria = miForm.cleaned_data.get("categoria")
            articuloPrecio = miForm.cleaned_data.get("precio")
            articuloDisponibilidad = miForm.cleaned_data.get("disponibilidad")
            articulo = Articulo(nombre=articuloNombre, categoria=articuloCategoria, precio=articuloPrecio, disponibilidad=articuloDisponibilidad)
            articulo.save()
            contexto = {'articulos': Articulo.objects.all()}
            return render(request, "articuloSucces.html", contexto)
    
    else:
        miForm = ArticuloForm()
    
    return render(request, "articuloForm.html", {"form": miForm})

def buscarArticulos(request):
    return render(request, "buscarArticulos.html")

def encontrarArticulos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        articulos = Articulo.objects.filter(nombre__icontains = patron)
        contexto = {"articulos": articulos}
        return render(request, "articulo.html", contexto)
    
    contexto = {'articulos': Articulo.objects.all()}
    return render(request, "articulo.html", contexto) 