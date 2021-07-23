from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import TodoForm
from .models import Todo


def index(request):
    return render(request, 'todo/index.html')


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
