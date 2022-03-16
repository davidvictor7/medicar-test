from diaryDoctor.api.serializers import DiaryDoctorSerializer
from diaryDoctor.models import DiaryDoctor, Times
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet


class DiaryDoctorViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DiaryDoctor.objects.prefetch_related(Prefetch(
        'hours', queryset=Times.objects.all())).all()
    serializer_class = DiaryDoctorSerializer
