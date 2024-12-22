from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    