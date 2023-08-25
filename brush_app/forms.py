from .models import Comment, Post, Profile
from django import forms


class CommentForm(forms.ModelForm):
    """
    A form for creating or editing comments on a post.

    Fields:
        body (TextField): The content of the comment.

    Meta:
        model (Comment): The Comment model to use for the form.
        fields (tuple):
        The fields from the Comment model to include in the form.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class ReportCommentForm(forms.Form):
    """
    A form for reporting a comment with a reason.

    Fields:
        reason (CharField): The reason for reporting the comment.
            This field is rendered as a textarea with 4 rows.
    """
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))


class ArtworkUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        is_required = kwargs.pop("is_required", True)
        super(ArtworkUploadForm, self).__init__(*args, **kwargs)
        self.fields['artwork_image'].required = is_required

    class Meta:
        model = Post
        fields = ['title', 'content', 'artwork_image']


class SearchForm(forms.Form):
    """
    A form for searching posts by providing a search query.

    Fields:
        search_query (CharField): The search query entered by the user.
            It allows a maximum length of 100 characters.
    """
    search_query = forms.CharField(label='Search Posts', max_length=100)


class ProfilePictureForm(forms.ModelForm):
    """
    A form for updating the profile picture of a user's profile.

    Fields:
        profile_picture (CloudinaryFileField): The new profile picture image.

    Meta:
        model (Profile): The Profile model to use for the form.
        fields (list):
        The fields from the Profile model to include in the form.
    """
    class Meta:
        model = Profile
        fields = ['profile_picture']
