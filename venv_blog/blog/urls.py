from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    # all post entries will start with "post/"
    path("post/<int:pk>", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
]
