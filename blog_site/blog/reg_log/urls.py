from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.registration, name = 'registration'),
    path('create',views.create,name='create'),
    path('api/v1/category/',views.CategoryViewSet.as_view({'get':'list'}),name='apicategory')
]
