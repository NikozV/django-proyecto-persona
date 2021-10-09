from django.shortcuts import render
from django.views import View
from .models import Persona
#Poner
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class PersonaView(View):

    #Saltar restricción csrf
    @method_decorator(csrf_exempt)
    #Creo metodo dispatch (Despachar/enviar)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #Listar personas - persona
    def get(self, request, id=0):
        if (id>0):
            personas=list(Persona.objects.filter(id=id).values())
            if len(personas)>0:
                persona=personas[0]
                datos={'message': 'Busqueda Exitosa', 'persona':persona}
            else:
                datos={'message':'No se encuentra a la persona'}
            return JsonResponse(datos)
        else:
            personas=list(Persona.objects.values())
            if len(personas)>0:
                datos={'message':'Exitoso', 'personas': personas}
            else:
                datos={'message':'No hay personas'}
            return JsonResponse(datos)
            #Crear metodo dispatch

    #Registrar personas
    def post(self, request):
        #print(request.body) #Probando respuesta
        #Cargar el json
        jd = json.loads(request.body)
        #print(jd) #probando respuesta
        #Cargo elemento
        Persona.objects.create(nombre=jd['nombre'], apellido=jd['apellido'])

        datos={'message':'Registro exitoso'}
        return JsonResponse(datos)

    #Actualizar persona
    def put(self, request, id):
        jd = json.loads(request.body)
        personas = list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            persona=Persona.objects.get(id=id)
            persona.nombre=jd['nombre']
            persona.apellido=jd['apellido']
            persona.save()
            datos = {'message': 'Exito'}
        else:
            datos = {'message':'Error, no existe la persona'}
        return JsonResponse(datos)

    #Eliminar persona
    def delete(self, request, id):
        personas = list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            Persona.objects.filter(id=id).delete()
            datos={'message':'Persona eliminada'}
        else:
            datos={'message':'Persona no encotrada'}
        return JsonResponse(datos)