from .models import Comment, Post, Profile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReportCommentForm(forms.Form):
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))


class ArtworkUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'artwork_image']


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search Posts', max_length=100)


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
