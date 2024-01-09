import django_filters
from .models import Resource

class ResourceFilter(django_filters.FilterSet):
  title = django_filters.CharFilter(lookup_expr='icontains')
  start_date = django_filters.DateFilter(field_name='pub_date', lookup_expr='gte')
  end_date = django_filters.DateFilter(field_name='pub_date', lookup_expr='lte')
  class Meta:
    model = Resource
    fields = ['type']