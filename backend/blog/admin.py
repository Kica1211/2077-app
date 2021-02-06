from django.contrib import admin
from .models import Post, Comment, Category, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ('pk', 'title', 'author')
    list_filter = ('category', )


admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(Category)

admin.site.site_header = "Blog Admin"
