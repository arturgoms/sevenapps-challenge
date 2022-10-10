from apps.domain.models.work_history.models import WorkHistory
from django.db.models import F
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

class CompanySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    
class CompaniesByPersonSerializer(serializers.Serializer):
    companies = serializers.ListField(child=CompanySerializer())
    
class CompaniesByPersonViewSet(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    serializer_class = CompaniesByPersonSerializer
    
    def get(self, request, person_id):  # noqa
        """
        Returns list of companies that the person_id works at
        """
        companies =  WorkHistory.objects.select_related('company').filter(person_id=person_id).annotate(
                company_name=F('company__name')
            ).values('id', 'company__name')
        
        data = {}
        data["companies"] = []
        
        for company in companies:
            data["companies"].append({
                "id": company["id"],
                "name": company["company__name"]
            })
        return Response(CompaniesByPersonSerializer(data).data)
