from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class mythread(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE) # on_delete=models.CASCADE
#Functionality: When the referenced object is deleted, all objects that reference it will also be deleted (i.e., cascading delete).
#Purpose: It ensures data integrity by preventing orphaned objects that reference deleted objects.
    text=models.TextField(max_length=240)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}' 
    
