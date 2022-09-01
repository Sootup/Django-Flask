from importlib.resources import contents
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import FirstDB
from .form import FirstDBForm


def index(request):
    # first=FirstDB.objects.all()
    first = FirstDB.objects.filter(title='Первое')
    return render(request, 'main/index.html', {'title':'Главная страница', 'first':first})

def second(request):
    return HttpResponse("<h4>Hello second world</h4>")


def add(request):
    if request.method =='POST':
        form=FirstDBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма не валинда'
            
    
    error= ''
    title = 'Страница добавления'
    form = FirstDBForm()
    
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/add.html', context)