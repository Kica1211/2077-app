from django.contrib.auth.models import User
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Post, Category, Comment, PostImage
from rest_framework import serializers


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'posts': ('blog.PostSerializer', {'many': True})
        }


class ImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class PostSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # set author as read-only field
        read_only_fields = ['id', 'created', 'author']
        expandable_fields = {
            'category': ('blog.CategorySerializer', {'many': True}),
            'comments': ('blog.CommentSerializer', {'many': True}),
            'images': ('blog.ImageSerializer', {'many': True}),
        }

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(
            author=user, title=validated_data['title'], content=validated_data['content'])
        post.category.set(validated_data['category'])
        return post

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.author.id:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission to change this post."})
        instance.category.set("")
        for ctg in validated_data['categories'].split(','):
            instance.category.add(Category.objects.get(pk=ctg))
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()
        return instance

    def delete(self, instance):
        user = self.context['request'].user
        if user.pk != instance.author.id:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission to delete this post."})
        instance.delete()


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'content', 'author', 'created', 'updated']
