from django.urls import path
from .views import PersonaView

urlpatterns = [
    path('persona/', PersonaView.as_view(), name='Personas_list'),
    path('persona/<int:id>', PersonaView.as_view(), name="Personas_process")
    
]
