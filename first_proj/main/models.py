from pydoc import describe
from tabnanny import verbose
from django.db import models

class FirstDB(models.Model):
    title=models.CharField('Название', max_length=50)
    descrp=models.TextField('Описание')    
    def __str__(self):
        return self.title 


    class Meta:
        verbose_name = 'Телевизор'
        verbose_name_plural = 'Телевизоры'