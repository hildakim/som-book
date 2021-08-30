from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField

# Create your models here.
class Book(models.Model):
    title = CharField(max_length=70)
    author = CharField(max_length=50)
    image = TextField()
    isbn = CharField(max_length=50, unique=True)
    price = IntegerField()
    pubdate = CharField(max_length=8)
    publisher = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        return self.title