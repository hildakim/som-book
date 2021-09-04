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
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),#TemplateView를 상속받아 정의
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),#ListView를 상속받아 정의

    path('addBookmark/<str:postId>', addBookmark,name='addBookmark'),
    path('deleteBookmark/<str:bookmarkId>', deleteBookmark,name='deleteBookmark'),

    path('bookmark/',bookmark,name="bookmark"),
]