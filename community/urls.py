from django.contrib import admin
from django.urls import path
from .views import *

app_name = "community"

urlpatterns = [
    path('', community, name="community"),
    path('<int:id>', detail, name="community_detail"),
    path('new/', new, name="community_new"),
    path('edit/<int:id>', edit, name="community_edit"),
    path('delete/<int:id>', delete, name="community_delete"),
]