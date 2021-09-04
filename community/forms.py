from django import forms
from .models import *

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title','contents','image', 'youtube_link', 'tags']

        widgets = {
            'contents': forms.Textarea(
            attrs={'placeholder': '커뮤니티 글을 작성해주세요.'}),

            'tags' : forms.TextInput(
            attrs={'placeholder': '태그는 쉼표(,)로 구분됩니다.'}),
        }

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields =[]
