from queryPatient.api.serializers import QueryPatientSerializer
from queryPatient.models import QueryPatient
from rest_framework.viewsets import ModelViewSet


class QueryPatientViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = QueryPatient.objects.all()
    serializer_class = QueryPatientSerializer
