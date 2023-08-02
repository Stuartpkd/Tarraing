from . import views
from django.urls import path

from .views import PostEdit


urlpatterns = [
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('post/<slug:slug>/edit/', PostEdit.as_view(), name='edit_post'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name='delete_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('upload/', views.Upload.as_view(), name='upload'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:post_slug>/save_artwork/', views.save_artwork,
         name='save_artwork'),
    path('', views.PostList.as_view(), name='home'),
]
