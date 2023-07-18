from django.contrib import admin
from .models import Post


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


admin.site.register(Post)

# Register your models here.
