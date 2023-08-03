from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Count
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Post, Profile, SavedArtwork
from .forms import CommentForm, ArtworkUploadForm


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        print(slug)
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter().order_by('created_on')
        has_saved_artwork = False
        if request.user.is_authenticated:
            has_saved_artwork = post.saved_artworks.filter(user=request.user).exists()
        liked = post.likes.filter(id=request.user.id).exists()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "has_saved_artwork": has_saved_artwork,
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


class CommentEdit(View):
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user != comment.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this comment.")

        form = CommentForm(instance=comment)

        return render(request, "post_view.html", {"form": form,
                                                  "comment": comment})

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user != comment.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this comment.")
            
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect("post_detail", slug=comment.post.slug)

        return render(request, "post_view.html", {"form": form,
                                                  "comment": comment})


class CommentDelete(view):
    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user != comment.author:
            return HttpResponseForbidden("You do not have permission"
                                         " to delete this comment.")
        
        comment.delete()
        return redirect("post_detail", slug=comment.post.slug)


class PostEdit(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this.")

        form = ArtworkUploadForm(instance=post)

        return render(request, "edit_post.html", {"form": form, "post": post})

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this.")

        form = ArtworkUploadForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=slug)

        return render(request, "edit_post.html", {"form": form, "post": post})


class PostDelete(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to delete this post.")

        post.delete()

        return redirect(reverse('profile',
                                kwargs={'username': request.user.username}))


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Upload(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(
            request,
            "upload.html",
            {
                "form": ArtworkUploadForm()
            },
        )

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()
        artwork_upload_form = ArtworkUploadForm(request.POST, request.FILES)

        if artwork_upload_form.is_valid():
            upload = artwork_upload_form.save(commit=False)
            upload.author = self.request.user
            upload.save()
            return redirect(reverse('home'))
        else:
            return render(request, 'upload.html', {'ArtworkUploadform':
                          Artwork_upload_form})


class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, username):
        profile = get_object_or_404(Profile, user__username=username)
        user_posts = profile.user.artwork_posts.all()
        total_likes_count = user_posts.aggregate(total_likes=Count
                                                 ('likes'))['total_likes']
        total_posts_count = user_posts.count()

        saved_artworks = SavedArtwork.objects.filter(user=request.user)

        return render(request,
                      self.template_name, {'profile': profile,
                                           'user_posts': user_posts,
                                           'total_likes_count': total_likes_count,
                                           'total_posts_count': total_posts_count,
                                           'saved_artworks': saved_artworks})


def save_artwork(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.user.is_authenticated:
        has_saved_artwork = SavedArtwork.objects.filter(user=request.user, post=post).exists()

        if not has_saved_artwork:
            SavedArtwork.objects.create(user=request.user, post=post)

    return redirect('post_detail', slug=post_slug)
