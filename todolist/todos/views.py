from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, "add.html")


# def delete_todo(request, pk):
#    todo = Todo.objects.get( pk=pk)
#    todo.delete()
#    return redirect("/")


class TodoDelete(DeleteView):
    model = Todo
    success_url = "/"


class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url ="/"
