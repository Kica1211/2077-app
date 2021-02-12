from django.urls import path
from gallery.views import GalleryViewSet
urlpatterns = [
    path('images/', GalleryViewSet.as_view(), name="images"),
]
