from webbrowser import get
from django.urls import path
from first_proj import views
from first_proj.views import index, get_form, starter # from . import views

urlpatterns = [
   path(r'index1/', index, name='index'),
   path(r'get_form/',get_form,name='forma'),
   path(r'',views.main),
]