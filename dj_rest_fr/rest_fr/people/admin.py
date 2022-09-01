from sre_constants import CATEGORY_SPACE
from django.contrib import admin

from .models import Category, user




admin.site.register(user)
admin.site.register(Category)