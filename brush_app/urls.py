from . import views
from django.urls import path

from .views import PostEdit, PostDelete, CommentEdit, CommentDelete, Upload, random_post_redirect, download_artwork, report_comment


urlpatterns = [
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('post/<slug:slug>/edit/', PostEdit.as_view(), name='edit_post'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name='delete_post'),
    path('comment/<int:comment_id>/edit/', views.CommentEdit.as_view(), name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.CommentDelete.as_view(), name='delete_comment'),
    path('report-comment/<int:post_id>/<slug:slug>/<int:comment_id>/', views.report_comment, name='report_comment'),
    path('search/', views.search_posts, name='search_posts'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('post-detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('random-post/', random_post_redirect, name='random_post_redirect'),
    path('download/<slug:post_slug>/', download_artwork, name='download_artwork'),
    path('save-post/<slug:post_slug>/', views.save_post, name='save_post'),
    path('unsave-post/<slug:post_slug>/', views.unsave_post, name='unsave_post'),
    path('upload', Upload.as_view(), name='upload'),
    path('', views.PostList.as_view(), name='home'),
]
