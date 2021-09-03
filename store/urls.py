from django.contrib import admin
from django.urls import path
from .views import *

app_name = "store"

urlpatterns = [
    path('', store, name="index"),
    path('<int:id>/<book_slug>',detail, name="detail"),
]