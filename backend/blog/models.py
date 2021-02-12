from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(default='default.jpg', upload_to='images')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    category = models.ManyToManyField(
        Category, related_name='posts', blank=True)
    categories = models.TextField(blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(
        Post, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
