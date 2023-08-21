from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models import Count, Q
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseForbidden, FileResponse, HttpResponse
from .models import Post, Profile, SavedArtwork, Comment, Upload
from .forms import CommentForm, ArtworkUploadForm, SearchForm, ProfilePictureForm, ReportCommentForm
import random


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        print(context)
        return context


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter().order_by('created_on')
        has_saved_artwork = False
        if request.user.is_authenticated:
            has_saved_artwork = SavedArtwork.objects.filter(user=request.user,
                                                            post=post).exists()
        liked = post.likes.filter(id=request.user.id).exists()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "has_saved_artwork": has_saved_artwork,
                "comment_form": CommentForm(),
                "user": request.user
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
                "comment_form": CommentForm(),
                "user": request.user
            },
        )


def search_posts(request):
    query = request.GET.get('q')
    form = SearchForm(request.GET)
    results = None

    if query is not None:
        args = Q(title__icontains=query)
        results = Post.objects.filter(args)
    else:
        results = None

    return render(request, 'search_results.html', {'results':
                                                   results, 'form': form})


def download_artwork(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.artwork_image:
        image_format = post.artwork_image.format
        public_id = post.artwork_image.public_id

        download_url = f"https://res.cloudinary.com/YOUR_CLOUD_NAME/image/upload/{public_id}.{image_format}"

        response = HttpResponse()
        response['Content-Disposition'] = f'attachment; filename="{post.title}.{image_format}"'
        response['X-Accel-Redirect'] = download_url
        return response
    else:
        return HttpResponseNotFound("Artwork not found")


class CommentEdit(View):
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.username != comment.name:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this comment.")

        form = CommentForm(instance=comment)

        return render(request, "edit_comment.html", {"form": form,
                                                     "comment": comment})

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.username != comment.name:
            return HttpResponseForbidden("You do not have permission "
                                         "to edit this comment.")

        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=comment.post.slug)

        return render(request, "edit_comment.html",
                      {"form": form, "comment": comment})


class CommentDelete(View):
    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.username != comment.name:
            return HttpResponseForbidden("You do not have permission"
                                         " to delete this comment.")

        comment.delete()
        return redirect("post_detail", slug=comment.post.slug)


def report_comment(request, post_id, slug, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    post = get_object_or_404(Post, id=post_id, slug=slug) 
    if request.method == 'POST':
        form = ReportCommentForm(request.POST)
        if form.is_valid():
            comment.reported = True
            comment.reported_reason = form.cleaned_data['reason']
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = ReportCommentForm()

    return render(request, 'report_comment.html', {'form': form, 'comment': comment, 'post': post})


class PostEdit(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this.")

        form = ArtworkUploadForm(instance=post)

        return render(request, "edit_post.html",
                      {"form": form, "post": post})

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this.")

        form = ArtworkUploadForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=slug)

        return render(request, "post_detail.html",
                      {"form": form, "post": post})


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


class Upload(CreateView):
    model = Post
    fields = ['title', 'content', 'artwork_image']
    template_name = 'upload_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('post_detail', slug=post.slug)


class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, username):
        profile = get_object_or_404(Profile, user__username=username)
        user_posts = profile.user.artwork_posts.all()
        total_likes_count = user_posts.aggregate(total_likes=Count
                                                 ('likes'))['total_likes']
        total_posts_count = user_posts.count()

        saved_artworks = SavedArtwork.objects.filter(user__id=request.user.id)

        return render(request,
                      self.template_name, {'profile': profile,
                                           'user_posts': user_posts,
                                           'total_likes_count': total_likes_count,
                                           'total_posts_count': total_posts_count,
                                           'saved_artworks': saved_artworks})


def upload_profile_picture(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST,
                                  request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)

    else:
        form = ProfilePictureForm(instance=profile)

    return render(request, 'upload_profile_picture.html', {'form': form})


def save_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if not request.user.savedartwork_set.filter(post=post).exists():
        SavedArtwork.objects.create(user=request.user, post=post)
        return redirect('post_detail', slug=post_slug)

    return redirect('post_detail', slug=post_slug)


def unsave_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    saved_post = request.user.savedartwork_set.filter(post=post).first()

    if saved_post:
        saved_post.delete()
        return redirect('post_detail', slug=post_slug)

    return redirect('post_detail', slug=post_slug)


def random_post_redirect(request):
    all_posts = list(Post.objects.all())
    random_post = random.choice(all_posts)
    return redirect(reverse('post_detail', kwargs={'slug': random_post.slug}))
