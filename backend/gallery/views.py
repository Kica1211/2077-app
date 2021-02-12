from django.shortcuts import render
from .serializers import GalleryImageSerializer
from .models import GalleryImage
from rest_framework.permissions import AllowAny
from rest_framework import generics


class GalleryViewSet(generics.ListAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
