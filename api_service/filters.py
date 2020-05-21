from django_filters import rest_framework as filters
from .models import BirthDay


class BirthdayDateFilter(filters.FilterSet):
    to_date = filters.DateFilter(field_name="birthday", lookup_expr='lte', input_formats=['%d%m%Y'])
    from_date = filters.DateFilter(field_name="birthday", lookup_expr='gte', input_formats=['%d%m%Y'])

    class Meta:
        model = BirthDay
        fields = ['from_date', 'to_date']
