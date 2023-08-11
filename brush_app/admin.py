from django.contrib import admin
from .models import Post, Comment, Profile, SavedArtwork, Upload, SavedPost
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

    list_display = ('name', 'body', 'post', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'profile_picture', 'num_likes',
                    'num_posts', 'num_downloads')
    search_fields = ('user__username',)
    list_filter = ('num_likes', 'num_posts', 'num_downloads')


@admin.register(SavedArtwork)
class SavedArtworkAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user__username', 'post__title')
    list_filter = ('user', 'post')


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'artwork_image')


@admin.register(SavedPost)
class SavedPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'saved_at')
    list_filter = ('user', 'post', 'saved_at')
    search_fields = ('user__username', 'post__title')
    readonly_fields = ('saved_at',)