from django.shortcuts import render

from todolist.models import Todolist


# Create your views here.

def index(req):
    todo_items = Todolist.objects.order_by('id')
    context = {'todo_items' : todo_items}
    return render(req,'todolist/index.html',context)

