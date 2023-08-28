from django.contrib import admin
from .models import Post, Comment, Profile, SavedArtwork, Upload
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_on']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post',
                    'created_on', 'reported', 'reported_reason')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def display_profile_picture(self, obj):
        return (
                str(obj.profile_picture)
                if obj.profile_picture
                else 'No Profile Picture'
                )
    display_profile_picture.short_description = 'Profile Picture'
    list_display = ('user', 'display_profile_picture',
                    'num_likes', 'num_posts')
    search_fields = ('user__username',)
    list_filter = ('num_likes', 'num_posts')


@admin.register(SavedArtwork)
class SavedArtworkAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user__username', 'post__title')
    list_filter = ('user', 'post')


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'artwork_image')
