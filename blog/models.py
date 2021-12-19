from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    population = models.IntegerField(null=True,default=0)
    address = models.TextField(null=True,max_length=250)
