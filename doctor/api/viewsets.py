from doctor.api.serializers import DoctorSerializer
from doctor.models import Doctor
from rest_framework.viewsets import ModelViewSet


class DoctorViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
