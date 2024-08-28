import django_filters 
from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    experience = django_filters.NumberFilter(field_name='experience', lookup_expr='gte')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['published_at','image','','employer','vacancy','salary','slug']
        