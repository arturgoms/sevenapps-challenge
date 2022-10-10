from apps.domain.models.company.models import Company
from rest_framework.response import Response
from rest_framework import viewsets, status, serializers

    
class InvestorsSerializer(serializers.Serializer):
    investors = serializers.ListField()
    

class InvertorsByCompanyViewSet(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    def get(self, request, company_id):  # noqa
        """
        Returns list of investors of company
        """
        
        company = Company.objects.get(id=company_id)
        
        investors = company.investors.split(",")
        data = {}
        data["investors"] = investors
        
        return Response(InvestorsSerializer(data).data)

