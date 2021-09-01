from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Community(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author', null=True)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "community/", blank = True, null = True)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.contents[:100]
