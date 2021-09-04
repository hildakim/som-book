from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

# Create your models here.

class Community(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author', null=True)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "community/", blank = True, null = True)
    tags = TaggableManager(blank=True)
    youtube_link = models.CharField(max_length=200,blank=True, null=True)

    class Meta:
        verbose_name = 'community' #테이블 단수 별칭
        verbose_name_plural = 'communities' #테이블 복수 별칭
        db_table = 'community_communities' #디폴트는 앱명_모델명(blog_post)
        ordering = ('-date',) #출력 시 modify_dt를 기준으로 내림차순 정렬
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.contents[:10]

    def get_previous(self):
        return self.get_previous_by_date()#장고의 내장함수, date()를 기준으로 최신포스트를 반환

    def get_next(self):
        return self.get_next_by_date()



class Bookmark(models.Model):
    
    postId = models.ForeignKey("Community",on_delete=models.CASCADE,db_column="postId")
    userId=models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.postId