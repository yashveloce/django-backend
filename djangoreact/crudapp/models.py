from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=20,null=True,blank=True)
    roll_no = models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return str(self.id)
