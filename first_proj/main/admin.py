# Админка джанго
from django.contrib import admin

from .models import FirstDB


admin.site.register(FirstDB) # Регистрация дб в админке