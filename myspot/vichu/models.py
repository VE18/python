from django.db import models

# Create your models here.
class index(models.Model):
    index = models.IntegerField()
    task = models.CharField(max_length=200)



