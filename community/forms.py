from django import forms
from .models import *

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title','contents','image', 'tags']

        widgets = {
            'contents': forms.Textarea(
            attrs={'placeholder': '커뮤니티 글을 작성해주세요.'}),
        }

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields =[]
