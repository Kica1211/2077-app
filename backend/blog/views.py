from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import PostSerializer, CategorySerializer
from .models import Post, Category
from rest_flex_fields import is_expanded
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


class PostViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permit_list_expands = ['category', 'comments', 'images']


class CategoryViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permit_list_expands = ['posts']


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        # this is the trick since you want to pass the request object to your serializer
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
