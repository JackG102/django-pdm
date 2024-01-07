from django.views import generic
from .models import Blog

# Define Blog views
class BlogDetailView(generic.DetailView):
  model = Blog
  template_name = "blog/detail.html"