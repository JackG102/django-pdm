from django.views import generic
from .models import Resource

# Create your views here.
# Define Blog views
class ResourceDetailView(generic.DetailView):
  model = Resource
  template_name = "resource_libary/detail.html"

class ResourceIndexView(generic.ListView):
  model = Resource
  template_name = "resource_library/index.html"
  paginate_by = 2
  context_object_name = "resources"