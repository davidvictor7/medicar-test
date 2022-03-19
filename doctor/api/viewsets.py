from django_filters.rest_framework import DjangoFilterBackend
from doctor.api.serializers import DoctorSerializer
from doctor.models import Doctor
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet


class DoctorViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
