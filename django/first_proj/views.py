from django.shortcuts import render
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import loader

def index(request):
   template = loader.get_template('1.html')
   context = {'title':'main'}
   return HttpResponse(template.render(context,request))

def get_form(request):
   value = request.POST.get('key')
   context = {'title':'formaa'}
   return HttpResponse(template.render(context,request))

   
# def starter(request):
#    return HttpResponse("<h4>HEllo</h4>")


def main(request):
   return render(request, 'main/1.html')






