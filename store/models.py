from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    title = CharField(max_length=300)
    author = CharField(max_length=50)
    slug = models.SlugField(max_length=300,unique=True,allow_unicode=True)
    image = TextField()
    isbn = CharField(max_length=50, unique=True)
    price = IntegerField()
    pubdate = CharField(max_length=20)
    publisher = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:detail',args=[self.id,self.slug])