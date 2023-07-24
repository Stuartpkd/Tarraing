from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):
    