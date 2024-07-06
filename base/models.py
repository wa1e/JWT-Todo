from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank = True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.title
    
    class META:
        ordering = ['complete']

class CustomUser(User):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed