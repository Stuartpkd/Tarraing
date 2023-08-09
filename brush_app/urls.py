from . import views
from django.urls import path

from .views import PostEdit, PostDelete, CommentEdit, CommentDelete, Upload


urlpatterns = [
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('post/<slug:slug>/edit/', PostEdit.as_view(), name='edit_post'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name='delete_post'),
    path('comment/<int:comment_id>/edit/', views.CommentEdit.as_view(), name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.CommentDelete.as_view(), name='delete_comment'),
    path('search/', views.search_posts, name='search_posts'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:post_slug>/save_artwork/', views.save_artwork,
         name='save_artwork'),
    path('<slug:post_slug>/unsave_artwork/', views.unsave_artwork, name='unsave_artwork'),
    path('upload', Upload.as_view(), name='upload'),
    path('', views.PostList.as_view(), name='home'),
]
