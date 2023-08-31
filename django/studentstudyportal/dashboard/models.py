#creating a database table 


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):   #class notes containning below 3 columns
    user = models.ForeignKey(User,on_delete=models.CASCADE)   #when this user is deleted then this notes also deleted from database
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):           #to display title name
        return self.title
    
    class Meta:         #for removing that extra s added by django admin
        verbose_name ="notes"    #new name
        verbose_name_plural = "notes"   #previous name
        
        

class Homework(models.Model):  #class homework containing below 6 col 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100) 
    description = models.TextField()       
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):  # to display title name
        return self.title


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):  # to display title name
        return self.title