from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=20, required = True)
    apellido = forms.CharField(max_length=20, required = True)
    email = forms.EmailField(required = True)
    numero = forms.IntegerField(required = True)
    direccion = forms.CharField(max_length=100, required = True)

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=20, required = True)
    apellido = forms.CharField(max_length=20, required = True)
    email = forms.EmailField(required = True)
    clave = forms.CharField(max_length=20, required = True, widget=forms.PasswordInput)
    numero = forms.IntegerField(required = True)
    direccion = forms.CharField(max_length=100, required = True)

class ArticuloForm(forms.Form):
    nombre = forms.CharField(max_length=20, required = True)
    categoria = forms.ChoiceField(choices=[
                        ("polera", "Polera"),
                        ("hoodie", "Hoodie"),
                        ("sueter", "Sueter"),
                        ("pantalon", "Pantalon"),
                        ("gorro", "Gorro"),
                        ("accesorio", "Accesorio")
                        ], required=True)
    precio = forms.IntegerField(required = True)
    disponibilidad = forms.BooleanField(required = True)