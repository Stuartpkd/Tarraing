from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BrushUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'brush_image', 'brush']
