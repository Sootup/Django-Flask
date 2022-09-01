from dataclasses import field
from .models import FirstDB
from django.forms import ModelForm, TextInput, Textarea


class FirstDBForm(ModelForm):            #Создание дб
    class Meta:
        model=FirstDB
        
        fields = ["title", "descrp"]
        
        widgets = {"title":TextInput(attrs={
            "class": 'form-control',
            "placeholder":"Введите значение"
        }),
            "descrp":Textarea(
                attrs={
                    'class':'form-contol',
                    'placeholder':'Введите описание'
                }
        )}