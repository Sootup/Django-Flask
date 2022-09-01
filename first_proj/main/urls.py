# Отправляет и принимает http
from django.urls import path
from . import views # точка импортит всё

urlpatterns = [

    path('', views.index, name ='index'),
    path('second', views.second),
    path('add', views.add)
]
