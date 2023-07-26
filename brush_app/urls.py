from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('brushes/', views.PostList.as_view(), name='brushes'),
    path('profile/', views.PostList.as_view(), name='profile'),
    path('upload/', views.PostList.as_view(), name='upload'),
    path('register/', views.PostList.as_view(), name='register'),
]
