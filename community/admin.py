from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'tag_list',)
    list_filter = ('date',)
    search_fields = ('title', 'content',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())

admin.site.register(Bookmark)

