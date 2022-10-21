from wsgiref.util import request_uri
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Category
from .serializers import CategorySerializer
from .forms import ArticleForm , UserCreationForm2
from django.contrib import messages
from django.http import HttpResponse 
from rest_framework import viewsets
def index(request):
    return render (request, 'auth/index.html')

class Registration(CreateView):
    form_class = UserCreationForm2
    success_url = reverse_lazy("index")
    template_name = "registration/registration.html"



def registration(request):
    flash = {'error':[]} # сюда добавить оповещения и т.д.
    form = UserCreationForm2(request.POST)
    # mes = messages.error(request,'nevernii')
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return index(request)   
        else:
            flash['error'].append('Пароль должен содержать не менее 8 символов,иметь заглавную букву и символ') 
            # error.append('Неверные данные')
            # messages.error(request,'nevernii')
            # mes = ['Неверный пароль']
            return render(request,"registration/registration.html",{'form': form, 'flash':flash})
    else:
        return render(request,"registration/registration.html",{'form': form})
   
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def create(request):
    flash= {'error':[]}
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            flash['error'].append('Форма невалидна')
    else:
        form = ArticleForm()
    return render(request, 'auth/create.html', {'form': form,'flash':flash})


    # def __init__(self, *args, **kwargs):
    #     super(Registration, self).__init__(*args, **kwargs)

        
    #     self.fields['username'].widget.attrs['class'] = 'form-control' 
    #     self.fields['password1'].widget.attrs['class'] = 'form-control' 
    #     self.fields['password2'].widget.attrs['class'] = 'form-control' 

# class MyUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['username'].help_text = ''
#         self.fields['password'].help_text = ''
    