from diaryDoctor.api.serializers import DiaryDoctorSerializer, TimesSerializer
from diaryDoctor.models import DiaryDoctor, Times
from django.db.models import Exists, OuterRef, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


class DiaryDoctorViewSet(ModelViewSet):

    queryset = DiaryDoctor.objects.all()
    serializer_class = DiaryDoctorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['doctor']

    freeHours = Times.objects.available().filter(
        diary=OuterRef('pk'), freeHour=True)

    queryset = DiaryDoctor.objects.available().prefetch_related(Prefetch(
        'hours', queryset=Times.objects.available())).filter(Exists(freeHours))


class TimesViewSet(ModelViewSet):

    queryset = Times.objects.all()
    serializer_class = TimesSerializer
