from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"


# detail view will provide us with a context object wich we can use for the template which will be called object 
# or we can use a word post
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


