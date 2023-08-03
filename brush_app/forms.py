from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ArtworkUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'artwork_image']


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search Posts', max_length=100)
