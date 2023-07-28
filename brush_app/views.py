from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, BrushUploadForm


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        print(slug)
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter().order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        print(slug)
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter().order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = Comment_Form()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# class Upload(View):
#     model = Post
#     template_name = 'upload.html'
#     fields = ['title', 'content', 'brush_image', 'brush']
#     success_url = reverse('home')

class Upload(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(
            request,
            "upload.html",
            {
                "form": BrushUploadForm()
            },
        )

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()
        brush_upload_form = BrushUploadForm(request.POST, request.FILES)

        if brush_upload_form.is_valid():
            upload = brush_upload_form.save(commit=False)
            selected_post_id = request.POST.get('selected_post')
            selected_post = get_object_or_404(Post, id=selected_post_id)
            upload.post = selected_post
            upload.save()
            return redirect('home')
        
        return render(
            request,
            "upload.html",
            {
                "post": post,
                "title": title,
                "content": content,
                "image": image,
                "brush": brush,
                "form": BrushUploadForm()
            },
        )
