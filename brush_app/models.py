from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryResource


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="artwork_posts")
    content = models.TextField()
    artwork_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,
                                   related_name='artwork_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Upload(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=200, unique=True)
    artwork_image = CloudinaryField('image', default='placeholder')


class SavedArtwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='savedartwork_set')

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=100, unique=True)
    num_likes = models.PositiveIntegerField(default=0)
    num_posts = models.PositiveIntegerField(default=0)
    num_downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_likes_count(self):
        self.num_likes = self.user.artwork_likes.count()

    def update_posts_count(self):
        self.num_posts = self.user.posts.count()

    def update_downloads_count(self):
        self.num_downloads = self.user.downloads.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

    instance.profile.save()
