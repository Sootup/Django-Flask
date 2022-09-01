from django.db import models


class user(models.Model): #BD
    title = models.CharField(max_length=250)
    context = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title


class Category(models.Model): # 2 bd
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name