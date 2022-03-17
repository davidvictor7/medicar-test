from datetime import date, datetime

from django.db import models
from django.db.models import Q
from django.utils import timezone


class DiaryManagement(models.Manager):
    def available(self):
        availableDay = super().get_queryset().filter(
            day__gte=date.today()).order_by('day')
        return availableDay


class HoursManagement(models.Manager):
    def available(self):
        timeFormat = datetime.strptime('00:00', '%H:%M')
        time = timezone.localtime(timezone.now())

        availableHour = super().get_queryset().filter(
            (
                Q(diary__day=date.today(), hour__gte=time) | Q(
                    diary__day__gt=date.today(), hour__gte=timeFormat)
            ),
            freeHour=True
        )
        return availableHour
