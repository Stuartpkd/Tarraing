from . import views
from django.urls import path


urlpatterns = [
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('upload/', views.Upload.as_view(), name='upload'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:post_slug>/save_brush/', views.save_brush, name='save_brush'),
    path('', views.PostList.as_view(), name='home'),
]
