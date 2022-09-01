from unittest.util import _MAX_LENGTH
from django.db import models

class First_db(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.TextField('Description')
