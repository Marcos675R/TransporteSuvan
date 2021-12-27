
from django.urls import path
from .views import contacto, index

urlpatterns = [
    path('index/', index, name='index'),
    path('contacto/',contacto, name='contacto' ),
]
