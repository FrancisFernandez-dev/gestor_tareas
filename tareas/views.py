from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import TareaForm

# "Base de datos" en memoria
TAREAS_POR_USUARIO = {}


# 1. Registro de usuario (signup)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # crea el usuario
            return redirect('login')  # redirige al login
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# 2. Lista de tareas
@login_required
def lista_tareas(request):
    user_id = request.user.id
    tareas = TAREAS_POR_USUARIO.get(user_id, [])
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})


# 3. Detalle de tarea
@login_required
def detalle_tarea(request, indice):
    user_id = request.user.id
    tareas = TAREAS_POR_USUARIO.get(user_id, [])

    try:
        tarea = tareas[indice]
    except IndexError:
        return redirect('lista_tareas')

    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'indice': indice})


# 4. Agregar tarea
@login_required
def agregar_tarea(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = {
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
            }
            lista = TAREAS_POR_USUARIO.get(user_id, [])
            lista.append(tarea)
            TAREAS_POR_USUARIO[user_id] = lista
            return redirect('lista_tareas')

    else:
        form = TareaForm()

    return render(request, 'tareas/tarea_form.html', {'form': form})


# 5. Eliminar tarea
@login_required
def eliminar_tarea(request, indice):
    user_id = request.user.id
    tareas = TAREAS_POR_USUARIO.get(user_id, [])

    if request.method == 'POST':
        try:
            tareas.pop(indice)
            TAREAS_POR_USUARIO[user_id] = tareas
        except IndexError:
            pass
        return redirect('lista_tareas')

    try:
        tarea = tareas[indice]
    except IndexError:
        return redirect('lista_tareas')

    return render(request, 'tareas/tarea_confirm_delete.html', {'tarea': tarea, 'indice': indice})
