from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(request):
    all_todo_item = TodoItem.objects.all()
    data = {
        'all_item':all_todo_item
    }
    return render(request,'todo.html',data)

def addTodo(request):
    new_item = TodoItem(content= request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')

    