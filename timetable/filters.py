from rest_framework import filters
from django.db.models import Q
from functools import reduce
from operator import or_

class SectionFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        filters = []
        for param, value in view.request.query_params.items():
                if param.startswith("section__"):
                    query_filter = Q(**{param: value})
                    filters.append(query_filter)
        if filters:
                combined_filter = reduce(or_, filters)
                queryset = queryset.filter(combined_filter)
                
        return queryset