from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    population = models.TextField(null=True,default=0)
    address = models.TextField(null=True,max_length=250)
    type = models.TextField(null=True,max_length=15)
    image = models.ImageField(upload_to="./static/images/",null=True,max_length=150)



class user(User):
    pass
