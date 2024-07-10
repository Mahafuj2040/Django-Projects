from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        # fields = '__all__'
        # fields = ['name', 'bio']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        # fields = '__all__'
        # fields = ['name', 'bio']
        