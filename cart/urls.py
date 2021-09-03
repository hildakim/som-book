from django.contrib import admin
from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path('',detail,name='detail'),
    path('add/<int:book_id>/',add,name='book_add'),
    path('remove/<book_id>/',remove,name='book_remove'),
    path('removeAll',remove_all,name="remove_all"),
]