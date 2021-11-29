from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm
from curso.models import Curso, Actuacion

def curso_nueva(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'])
            for alumno_id in request.POST.getlist('alumnos'):
                actuacion = Actuacion(alumno_id=alumno_id, curso_id = curso.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'curso/curso_editar.html', {'formulario': formulario})