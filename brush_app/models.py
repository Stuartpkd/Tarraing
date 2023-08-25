from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryResource
from django.utils.text import slugify
import random
import string


class Post(models.Model):
    """
    Represents an artwork post submitted by users.

    Fields:
        title (CharField): The title of the post.
        slug (SlugField): A URL-friendly representation of the title.
        author (ForeignKey): The user who authored the post.
        content (TextField): The content of the post.
        artwork_image (CloudinaryField): The uploaded artwork image.
        created_on (DateTimeField): The date and time of post creation.
        likes (ManyToManyField): Users who have liked this post.

    Methods:
        number_of_likes(): Returns the count of likes on this post.
        generate_unique_slug(): Generates a unique slug for the post.
        save(*args, **kwargs): Overrides the save method to set a unique slug.
    """

    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="artwork_posts")
    content = models.TextField()
    artwork_image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,
                                   related_name='artwork_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Returns the count of likes on this post.
        """
        return self.likes.count()

    def generate_unique_slug(self):
        """
        Generates a unique slug for the post by combining the base slug
        derived from the title and a random suffix.
        """
        base_slug = slugify(self.title)
        random_suffix = ''.join(random.choices(string.ascii_lowercase +
                                               string.digits, k=6))
        return f"{base_slug}-{random_suffix}"

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set a unique slug if it's not provided.
        Also, updates the slug if the title changes.
        """
        # Check if the title has changed
        if self.id:
            old_post = Post.objects.get(pk=self.id)
            if old_post.title != self.title:
                self.slug = None  # Reset slug so it gets regenerated

        if not self.slug:
            unique_slug = self.generate_unique_slug()
            while (
                Post.objects.filter(slug=unique_slug)
                .exclude(id=self.id)
                .exists()
            ):
                unique_slug = self.generate_unique_slug()

                unique_slug = self.generate_unique_slug()
            self.slug = unique_slug

        super().save(*args, **kwargs)


class Upload(models.Model):
    """
    Represents an uploaded artwork with title, content, and image.

    Fields:
        title (CharField): The title of the artwork.
        content (TextField): A brief content description of the artwork.
        artwork_image (CloudinaryField): The uploaded artwork image.

    """
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=200, unique=True)
    artwork_image = CloudinaryField('image', default='placeholder')


class SavedArtwork(models.Model):
    """
    Represents the relationship between a user and a saved artwork post.

    Fields:
        user (ForeignKey): The user who saved the artwork.
        post (ForeignKey): The saved artwork post.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='savedartwork_set')

    def __str__(self):
        """
        Returns a formatted string representation of the saved artwork.
        """
        return f"{self.user.username} - {self.post.title}"


class Comment(models.Model):
    """
    Represents a comment on a post.

    Fields:
        post (ForeignKey): The post that this comment belongs to.
        name (CharField): The name of the commenter.
        email (EmailField): The email address of the commenter.
        body (TextField): The content of the comment.
        created_on (DateTimeField):
        The date and time when the comment was created.
        reported (BooleanField): Indicates if the comment has been reported.
        reported_reason (TextField, optional):
        The reason for reporting the comment.

    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    reported = models.BooleanField(default=False)
    reported_reason = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """
        Returns a formatted string representation of the comment.
        """
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    """
    Represents a user profile containing various statistics and information.

    Fields:
        user (OneToOneField): The user associated with this profile.
        profile_picture (CloudinaryField): The profile picture image.
        slug (SlugField): A URL-friendly representation of the user's username.
        num_likes (PositiveIntegerField): Number of likes received by the user.
        num_posts (PositiveIntegerField):
        Number of posts submitted by the user.
        num_downloads (PositiveIntegerField):
        Number of downloads initiated by the user.

    Methods:
        update_likes_count():
        Updates the num_likes count based on user's artwork likes.
        update_posts_count():
        Updates the num_posts count based on user's posts.
        update_downloads_count():
        Updates the num_downloads count based on user's downloads.
        save(*args, **kwargs): Overrides the save method to set a unique slug.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image')
    slug = models.SlugField(max_length=100, unique=True)
    num_likes = models.PositiveIntegerField(default=0)
    num_posts = models.PositiveIntegerField(default=0)
    num_downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_likes_count(self):
        """
        Updates the num_likes count based on the user's artwork likes.
        """
        self.num_likes = self.user.artwork_likes.count()

    def update_posts_count(self):
        """
        Updates the num_posts count based on the user's posts.
        """
        self.num_posts = self.user.posts.count()

    def update_downloads_count(self):
        """
        Updates the num_downloads count based on the user's downloads.
        """
        self.num_downloads = self.user.downloads.count()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set a unique slug based on the username.
        """
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a user profile upon user creation.

    Args:
        sender: The sender of the signal (User model).
        instance: The instance of the User model (the created user).
        created (bool): Indicates if the user was just created.
        kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)

    instance.profile.save()
