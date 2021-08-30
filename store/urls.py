from django.contrib import admin
from django.urls import path
from .views import *

app_name = "store"

urlpatterns = [
    path('', store, name="index"),
    path('detail/<int:id>', detail, name="detail"),
]