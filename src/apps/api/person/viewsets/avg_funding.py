from rest_framework import viewsets, status

from django.http import JsonResponse
from apps.domain.models.work_history.models import WorkHistory

class AverageFundingByPersonViewSet(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    def get(self, request, person_id):  # noqa
        """
        Returns whether the service is health.
        """

        avg = WorkHistory.objects.raw(
            """SELECT w.id, p.name, AVG(c.know_total_funding)
                FROM "work_history" AS w
            JOIN company as c
                on c.id = w.company_id
            JOIN "Person" as p
                on p.id = w.person_id
            WHERE 
                w.person_id = %s
            GROUP BY 
                p.name, w.id""", [person_id]
        )
        # TODO: Create serializer
        return JsonResponse({"name": avg[0].name, "avg": avg[0].avg if avg[0].avg else 0})
