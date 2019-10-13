from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'image')
        widgets = {
            'caption':forms.Textarea()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)