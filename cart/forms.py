from django import forms

class AddBookForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)