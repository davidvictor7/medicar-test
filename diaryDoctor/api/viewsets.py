from diaryDoctor.api.serializers import DiaryDoctorSerializer, TimesSerializer
from diaryDoctor.models import DiaryDoctor, Times
from django.db.models import Exists, OuterRef, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class DiaryDoctorViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DiaryDoctor.objects.all()
    serializer_class = DiaryDoctorSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['doctor']

    freeHours = Times.objects.available().filter(
        diary=OuterRef('pk'), freeHour=True)

    queryset = DiaryDoctor.objects.available().prefetch_related(Prefetch(
        'hours', queryset=Times.objects.available())).filter(Exists(freeHours))

    # queryset = DiaryDoctor.objects.prefetch_related(Prefetch(
    #     'hours', queryset=Times.objects.all())).all()
    # serializer_class = DiaryDoctorSerializer


class TimesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Times.objects.all()
    serializer_class = TimesSerializer
