from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('brushes/', views.PostList.as_view(), name='brushes'),
    path('profile/', views.PostList.as_view(), name='profile'),
    path('upload/', views.PostList.as_view(), name='upload'),
    path('register/', views.PostList.as_view(), name='register'),
]