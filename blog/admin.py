from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'date_create', 'slug', 'image', 'image_img')


admin.site.register(Post, PostAdmin)
