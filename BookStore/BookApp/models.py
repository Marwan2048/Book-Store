from django.db import models 
from django.contrib.auth.models import User


class Book(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField( max_length = 100 )
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add= True , blank=True)




