from django.db import models 
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Book(models.Model):

    author = models.ForeignKey(User , on_delete = models.SET_NULL , null=True)
    title = models.CharField( max_length = 100 )
    price = models.PositiveIntegerField(validators= [MinValueValidator(1)])
    description = models.TextField()
    created_at = models.DateField(auto_now_add= True , blank=True)

    def __str__(self):
        return self.title


