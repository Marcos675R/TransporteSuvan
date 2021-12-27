from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Contacto
from .models import Reservas, Servicio
# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ["nombreServicio", "precio", "descripcion", "servicio"] 
    lis_editable = ["precio"]
    search_fields = ["nombreServicio"]
    list_filter =["servicio"]
    list_per_page = 5


admin.site.register(Contacto)
admin.site.register(Servicio)
admin.site.register(Reservas)