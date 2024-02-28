from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo

def get_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def view_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})


def delete_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect('get_todos')
