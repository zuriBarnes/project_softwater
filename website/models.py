from django.db import models

# Create your models here.

class Leader(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    role = models.CharField(max_length=40)
    bio = models.TextField(default="bio needed")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
class Coach(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    role = models.CharField(max_length=40)
    bio = models.TextField(default="bio needed")
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"





