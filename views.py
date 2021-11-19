from django.shortcuts import render
from .forms import TaskForm

# Create your views here.
def view_todos(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/index.html', context)


def update_todo(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/update.html', context)


def delete_todo(request):
    return render(request, 'todo/delete.html')