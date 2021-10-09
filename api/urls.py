from django.urls import path
from .views import PersonaView

urlpatterns = [
    path('personas/', PersonaView.as_view(), name='Personas_list'),
    path('personas/<int:id>', PersonaView.as_view(), name="Personas_process")
    
]
