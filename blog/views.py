from django.views import generic
from .models import Blog

# Define Blog views
class BlogDetailView(generic.DetailView):
  model = Blog
  template_name = "blog/detail.html"

class BlogIndexView(generic.ListView):
  model = Blog
  template_name = "blog/index.html"
  paginate_by = 2
  context_object_name = "blogs"
