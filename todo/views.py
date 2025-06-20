from django.shortcuts import render
from .models import Todo
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})