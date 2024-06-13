from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30,blank=False)
    course = models.CharField(max_length=30,blank=False)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']