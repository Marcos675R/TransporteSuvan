from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ContactoForm
from .models import Reservas

# Create your views here.
def index(request):
    reservas = Reservas.objects.all()
    dataReserva = {
        'reservas' : reservas
    }

    return render(request, 'app/index.html', dataReserva)

def contacto(request):
    return render(request, 'app/contacto.html')

def contacto (request):
    data ={
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] ="Mensaje Enviado"
        
        else :
            data["form"]= formulario
    return render (request, 'app/contacto.html', data)
