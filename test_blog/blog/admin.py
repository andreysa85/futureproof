from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_name', 'post', 'author', 'time_creation',
                    'time_publication', 'time_update', 'image')


class TagAdmin (admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Post, PostAdmin)
