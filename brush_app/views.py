from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models import Count, Q
from django.views import generic, View
from django.urls import reverse
from django.http import (
    HttpResponseRedirect,
    HttpResponseForbidden,
    FileResponse,
    HttpResponse,
    JsonResponse,
)
from .models import Post, Profile, SavedArtwork, Comment, Upload
from .forms import (
    CommentForm,
    ArtworkUploadForm,
    SearchForm,
    ProfilePictureForm,
    ReportCommentForm,
)
import random


class PostList(generic.ListView):
    """
    View that displays a list of posts in a paginated manner.

    Attributes:
        model (Post): The Post model to query for the list of posts.
        template_name (str): The template used to render the list of posts.
        paginate_by (int): The number of posts to display per page.
    """
    model = Post
    template_name = 'index.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """
        Adds the search form to the context and returns it.

        Returns:
            dict: The context data dictionary.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


class PostDetail(View):
    """
    View for displaying details of a single post.

    Methods:
        get(request, slug, *args, **kwargs):
        Handles GET requests for the post detail page.
        post(request, slug, *args, **kwargs):
        Handles POST requests for adding comments to the post.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Handles GET requests for the post detail page.

        Args:
            request: The incoming HTTP request object.
            slug: The slug of the requested post.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The rendered post detail page.
        """
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter().order_by('created_on')
        has_saved_artwork = False
        if request.user.is_authenticated:
            has_saved_artwork = SavedArtwork.objects.filter(user=request.user,
                                                            post=post).exists()
        liked = post.likes.filter(id=request.user.id).exists()
        comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "has_saved_artwork": has_saved_artwork,
                "comment_form": comment_form,
                "user": request.user
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handles POST requests for adding comments to the post.

        Args:
            request: The incoming HTTP request object.
            slug: The slug of the post to comment on.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The rendered post detail page.
        """
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter().order_by('created_on')
        liked = post.likes.filter(id=self.request.user.id).exists()
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": comment_form,
                "user": request.user
            },
        )


def search_posts(request):
    """
    View function for searching posts based on a search query.

    Args:
        request: The incoming HTTP request object.

    Returns:
        HttpResponse: The rendered search results page.
    """
    query = request.GET.get('q')
    form = SearchForm(request.GET)
    results = None

    if query:
        args = Q(title__icontains=query)
        results = Post.objects.filter(args)
    else:
        results = []

    return render(request, 'search_results.html', {'results':
                                                   results, 'form': form})


def download_artwork(request, post_slug):
    """
    View function for downloading artwork image associated with a post.

    Args:
        request: The incoming HTTP request object.
        post_slug (str):
        The slug of the post whose artwork is to be downloaded.

    Returns:
        HttpResponse:
        The HTTP response containing the downloadable artwork image.
    """
    post = get_object_or_404(Post, slug=post_slug)

    if post.artwork_image:
        image_format = post.artwork_image.format
        public_id = post.artwork_image.public_id

        download_url = (
           "https://res.cloudinary.com/YOUR_CLOUD_NAME/image/upload/"
           f"{public_id}.{image_format}"
        )

        response = HttpResponse()
        response['Content-Disposition'] = (
            f'attachment; '
            f'filename="{post.title}.{image_format}"'
        )
        response['X-Accel-Redirect'] = download_url
        return response
    else:
        return HttpResponseNotFound("Artwork not found")


class CommentEdit(View):
    """
    View for editing a comment.

    Methods:
        get(request, comment_id, *args, **kwargs):
        Handles GET requests for editing a comment.
        post(request, comment_id, *args, **kwargs):
        Handles POST requests for updating a comment.
    """
    def get(self, request, comment_id, *args, **kwargs):
        """
        Handles GET requests for editing a comment.

        Args:
            request: The incoming HTTP request object.
            comment_id: The ID of the comment to be edited.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The rendered comment edit page.
        """
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.username != comment.name:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this comment.")

        form = CommentForm(instance=comment)

        return render(request, "edit_comment.html", {"form": form,
                                                     "comment": comment})

    def post(self, request, comment_id, *args, **kwargs):
        """
        Handles POST requests for updating a comment.

        Args:
            request: The incoming HTTP request object.
            comment_id: The ID of the comment to be updated.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse:
            The rendered comment edit page or a
            redirect to the post detail page.
        """
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.username != comment.name:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this comment.")

        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=comment.post.slug)

        return render(request, "edit_comment.html", {"form": form,
                                                     "comment": comment})


class CommentDelete(View):
    """
    View for deleting a comment.

    Methods:
        post(request, comment_id, *args, **kwargs):
        Handles POST requests for deleting a comment.
    """
    def post(self, request, comment_id, *args, **kwargs):
        """
        Handles POST requests for deleting a comment.

        Args:
            request: The incoming HTTP request object.
            comment_id: The ID of the comment to be deleted.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse:
            A redirect to the post detail page after deleting the comment.
        """
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.username != comment.name:
            return HttpResponseForbidden("You do not have permission "
                                         "to delete this comment.")

        comment.delete()
        return redirect("post_detail", slug=comment.post.slug)


def report_comment(request, post_id, slug, comment_id):
    """
    View for reporting a comment.

    Args:
        request: The incoming HTTP request object.
        post_id: The ID of the related post.
        slug: The slug of the related post.
        comment_id: The ID of the comment to be reported.

    Returns:
        HttpResponse:
        A rendered report comment page or a redirect to the post detail page.
    """
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

    return render(request, 'report_comment.html', {'form': form,
                                                   'comment': comment,
                                                   'post': post})


class PostEdit(View):
    """
    View for editing a post.

    Methods:
        get(request, slug, *args, **kwargs):
        Handles GET requests for editing a post.
        post(request, slug, *args, **kwargs):
        Handles POST requests for editing a post.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Handles GET requests for editing a post.

        Args:
            request: The incoming HTTP request object.
            slug: The slug of the post to be edited.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: A rendered edit post page.
        """
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this.")

        form = ArtworkUploadForm(instance=post)

        return render(request, "edit_post.html", {"form": form, "post": post})

    def post(self, request, slug, *args, **kwargs):
        """
        Handles POST requests for editing a post.

        Args:
            request: The incoming HTTP request object.
            slug: The slug of the post to be edited.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse:
            A redirect to the post detail page after successful
            edit or a rendered edit post page with errors.
        """
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to edit this.")

        form = ArtworkUploadForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            artwork_image = form.cleaned_data.get('artwork_image')

            if artwork_image:
                allowed_image_types = ['image/jpeg', 'image/png']
                if artwork_image.content_type not in allowed_image_types:
                    return JsonResponse({'error': 'Please upload '
                                         'a valid image file (JPEG, PNG)'})

                max_file_size = 1024 * 1024  # 1MB in bytes
                if artwork_image.size > max_file_size:
                    return JsonResponse({'error': 'The uploaded '
                                         'image is too large. Please '
                                         'upload an image under 1MB.'})

            form.save()
            return JsonResponse({'redirect_url': reverse('post_detail', args=[slug])})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'errors': errors})


class PostDelete(View):
    """
    View for deleting a post.

    Methods:
        post(request, slug, *args, **kwargs):
        Handles POST requests for deleting a post.
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Handles POST requests for deleting a post.

        Args:
            request: The incoming HTTP request object.
            slug: The slug of the post to be deleted.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: A redirect to the user's profile page after
            successful post deletion or a forbidden response.
        """
        post = get_object_or_404(Post, slug=slug)

        if request.user != post.author:
            return HttpResponseForbidden("You do not have "
                                         "permission to delete this post.")

        post.delete()

        return redirect(reverse('profile',
                                kwargs={'username': request.user.username}))


class PostLike(View):
    """
    View for handling post likes.

    Methods:
        post(request, slug): Handles POST requests for toggling post likes.
    """
    def post(self, request, slug):
        """
        Handles POST requests for toggling post likes.

        Args:
            request: The incoming HTTP request object.
            slug: The slug of the post to be liked/unliked.

        Returns:
            HttpResponseRedirect:
            A redirect to the post's detail page
            after handling the like action.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Upload(CreateView):
    """
    View for uploading new artwork posts.

    Methods:
        form_valid(form):
        Handles form validation and
        saving of the new artwork post.
    """
    model = Post
    fields = ['title', 'content', 'artwork_image']
    template_name = 'upload_form.html'

    def form_valid(self, form):
        """
        Handles form validation and saving of the new artwork post.

        Args:
            form: The validated form containing the artwork post data.

        Returns:
            HttpResponse:
            A redirect to the newly created post's detail page if successful,
            or a JSON response with an error message if validation fails.
        """
        artwork_image = form.cleaned_data.get('artwork_image')

        if not artwork_image:
            return JsonResponse({'error':
                                 'Please upload an image for your artwork.'})

        allowed_image_types = ['image/jpeg', 'image/png']
        if artwork_image.content_type not in allowed_image_types:
            return JsonResponse({'error': 'Please upload '
                                 'a valid image file (JPEG, PNG)'})

        max_file_size = 1024 * 1024  # 1MB in bytes
        if artwork_image.size > max_file_size:
            return JsonResponse({'error': 'The uploaded image is too large.'
                                 'Please upload an image under 1MB.'})

        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return JsonResponse({'redirect_url': reverse('post_detail', args=[post.slug])})
        
    def form_invalid(self, form):
        errors = dict(form.errors.items())
        return JsonResponse({'errors': errors})


class ProfileView(View):
    """
    View for displaying user profiles and associated artwork posts.

    Attributes:
        template_name (str): The name of the template to render.

    Methods:
        get(request, username):
        Handles the GET request to display the
        user's profile and artwork posts.
    """
    template_name = 'profile.html'

    def get(self, request, username):
        """
        Handles the GET request to display
        the user's profile and artwork posts.

        Args:
            request: The HTTP GET request object.
            username (str): The username of
            the user whose profile is being viewed.

        Returns:
            HttpResponse: A rendered template displaying
            the user's profile and artwork posts.
        """
        profile = get_object_or_404(Profile, user__username=username)
        user_posts = profile.user.artwork_posts.all()
        total_likes_count = user_posts.aggregate(total_likes=Count
                                                 ('likes'))['total_likes']
        total_posts_count = user_posts.count()

        saved_artworks = SavedArtwork.objects.filter(user__id=request.user.id)

        return render(
            request,
            self.template_name, {
                'profile': profile,
                'user_posts': user_posts,
                'total_likes_count': total_likes_count,
                'total_posts_count': total_posts_count,
                'saved_artworks': saved_artworks
            }
        )


def upload_profile_picture(request):
    """
    View for uploading and updating a user's profile picture.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A rendered template displaying the profile picture upload form.
    """
    profile = get_object_or_404(Profile, user=request.user)

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
    """
    View for saving a post to a user's saved artworks.

    Args:
        request: The HTTP request object.
        post_slug (str): The slug of the post to be saved.

    Returns:
        HttpResponse: A redirect to the post's detail page.
    """
    post = get_object_or_404(Post, slug=post_slug)

    if not request.user.savedartwork_set.filter(post=post).exists():
        SavedArtwork.objects.create(user=request.user, post=post)
        return redirect('post_detail', slug=post_slug)

    return redirect('post_detail', slug=post_slug)


def unsave_post(request, post_slug):
    """
    View for removing a saved post from a user's saved artworks.

    Args:
        request: The HTTP request object.
        post_slug (str): The slug of the post to be unsaved.

    Returns:
        HttpResponse: A redirect to the post's detail page.
    """
    post = get_object_or_404(Post, slug=post_slug)
    saved_post = request.user.savedartwork_set.filter(post=post).first()

    if saved_post:
        saved_post.delete()
        return redirect('post_detail', slug=post_slug)

    return redirect('post_detail', slug=post_slug)


def random_post_redirect(request):
    """
    View for redirecting to a random post's detail page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A redirect to a randomly selected post's detail page.
    """
    all_posts = list(Post.objects.all())
    random_post = random.choice(all_posts)
    return redirect(reverse('post_detail', kwargs={'slug': random_post.slug}))

