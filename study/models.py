from django.db import models

# Create your models here.

class Students(models.Model):
   name = models.CharField(max_length=10)
   address = models.CharField(max_length=50)
   email = models.CharField(max_length=30)

class Score(models.Model):
   student = models.ForeignKey(Students, on_delete=models.CASCADE)
   subject = models.CharField(max_length=10)
   score = models.IntegerField()
   created_at = models.DateTimeField(auto_now_add=True)
