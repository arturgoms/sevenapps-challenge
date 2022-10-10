from django.urls import path

from apps.api.person.viewsets.avg_funding import AverageFundingByPersonViewSet
from apps.api.person.viewsets.companies import CompaniesByPersonViewSet


urlpatterns = [
    path(
        "avg-funding-by-person/<uuid:person_id>",
        AverageFundingByPersonViewSet.as_view({'get': 'get'}),
        name="avg-funding-by-person",
    ),
    path(
        "companies-by-person/<uuid:person_id>",
        CompaniesByPersonViewSet.as_view({'get': 'get'}),
        name="companies-by-person",
    ),
    
]
