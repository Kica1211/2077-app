from django.urls import path
from blog.views import PostCreate, PostUpdate, PostDelete
urlpatterns = [
    path('post-create/', PostCreate.as_view(), name="post-create"),
    path('post-update/<int:pk>/', PostUpdate.as_view(), name="post-update"),
    path('post-delete/<int:pk>/', PostDelete.as_view(), name="post-delete"),
]
