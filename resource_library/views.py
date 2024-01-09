from django.shortcuts import render
from django.views import generic
from .filters import ResourceFilter
from .models import Resource

# Create your views here.
# Define Blog views
class ResourceDetailView(generic.DetailView):
  model = Resource
  template_name = "resource_library/detail.html"

def resource_library(request):
  resources = Resource.objects.all()
  myFilter = ResourceFilter(request.GET, queryset=Resource.objects.all())
  resources = myFilter.qs
  context = { 'myFilter': myFilter, 'resources': resources }
  return render(request, 'resource_library/index.html', context)