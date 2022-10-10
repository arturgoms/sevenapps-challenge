from django.urls import path

from apps.api.company.viewsets.inverstors import InvertorsByCompanyViewSet


urlpatterns = [
    path(
        "investors-by-company/<uuid:company_id>",
        InvertorsByCompanyViewSet.as_view({'get': 'get'}),
        name="investors-by-company",
    )
    
]
