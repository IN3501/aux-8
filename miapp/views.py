from django.shortcuts import render
from .models import Estudiante, Proyecto, Grupo, Desafio, DesafiosEstudiantes,Ramo
#from .models import Proyecto


# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def added_project(request):
	return render(request, 'miapp/added_project.html')



def add_proyecto(request):
	descripcion = request.POST['descripcion']
	cliente =request.POST['cliente']
	fecha = request.POST['fecha_limite']

	contexto = {"form":"Formulario creado con exito", "gracias":"Muchas gracias",
	 "descripcion":descripcion, "cliente":cliente, "fecha":fecha}
	
	proyecto = Proyecto(descripcion=descripcion, cliente=cliente, fecha_limite=fecha)
	proyecto.save()
	
	return render(request, 'miapp/added_project.html', contexto)




def new_project(request):
	return render(request, 'miapp/new_project.html')

def lista_estudiantes(request):
	contexto={}
	contexto['estudiantes'] = Estudiante.objects.all()
	return render(request, 'miapp/lista_estudiantes.html',contexto)

def lista_proyectos(request):
	contexto={}
	contexto['proyectos'] = Proyecto.objects.filter(fecha_limite__year__gt=2018,fecha_limite__month__exact=5)
	return render(request, 'miapp/lista_proyectos.html', contexto)

def added_ramo(request):
	return render(request, 'miapp/added_ramo.html')

def add_ramo(request):
	nombre = request.POST['nombre']
	departamento =request.POST['departamento']
	uds = request.POST['uds']

	contexto = {"form":"Formulario creado con exito", "gracias":"Muchas gracias"}
	
	proyecto = Ramo(nombre_ramo=nombre, departamento=departamento, uds=uds)
	proyecto.save()
	
	return render(request, 'miapp/added_ramo.html', contexto)

def new_ramo(request):
	return render(request, 'miapp/new_ramo.html')

def modificar_ramo(request):
	a_modificar = request.POST['nombre_antes']
	nuevo_nombre = request.POST['nombre_nuevo']
	registro= Ramo.objects.get(nombre_ramo=a_modificar)
	registro.nombre_ramo=nuevo_nombre
	registro.save()
	return render(request, 'miapp/added_ramo.html')
