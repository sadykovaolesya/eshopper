from .models import Comment
from django import forms
from django.forms import TextInput, Textarea   


class HiddenForm(forms.Form):
    parent_id = forms.IntegerField(widget=forms.HiddenInput)

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget = TextInput(attrs= {'placeholder':'write your name...'})
        self.fields['email'].widget = TextInput(attrs={'placeholder':'your email address...'})
        self.fields['body'].widget = Textarea(attrs={'placeholder':'write your commit...'})
        
    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')

