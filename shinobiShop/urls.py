from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("tienda/", shop, name="shop"),

    #FORMULARIOS
    path("cliente_form/", clienteForm, name="cliente_form"),
    path("ver_clientes/", verClientes, name="ver_cliente"),

    path("usuario_form/", usuarioForm, name="usuario_form"),
    path("ver_usuarios/", verUsuarios, name="ver_usuario"),

    path("articulo_form/", articuloForm, name="articulo_form"),
    path("ver_articulos/", verArticulos, name="ver_articulo"),
    path("buscar/", buscarArticulos, name="buscar_articulo"),
    path("encontrar/", encontrarArticulos, name="encontrar_articulo"),
]
