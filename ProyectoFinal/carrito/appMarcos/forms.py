from django import forms
from .models import  Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre", "correo","tipo_consulta", "mensaje", "avisos"]
        #fields = '__all__' (reemplazo el field de arriba)

class LoginForm(forms.Form):
    nombre= forms.CharField(widget=forms.TextInput)
    password= forms.CharField(widget=forms.PasswordInput)