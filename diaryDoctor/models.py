from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from doctor.models import Doctor

from diaryDoctor.management import DiaryManagement, HoursManagement


# Create your models here.
class DiaryDoctor(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    freeDay = models.BooleanField(default=True)
    objects = DiaryManagement()

    def clean(self):
        def validate_date():
            if self.day < date.today():
                raise ValidationError(
                    {'Data precisa ser maior a data atual'})

        def validate_diary_doc():
            try:
                diaryDoc = DiaryDoctor.objects.filter(
                    medico=self.doctor, dia=self.day).get()
                raise ValidationError(
                    {'Médico já possue uma agenda marcada'})
            except diaryDoc.DoesNotExist:
                pass

        validate_date()

        if self.id == None:
            validate_diary_doc()

    def __str__(self):
        return f"Agenda {self.id} - {self.day} / Medico: {self.doctor}"


class Times(models.Model):
    diary = models.ForeignKey(
        DiaryDoctor, related_name='hours', on_delete=models.CASCADE)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    freeHour = models.BooleanField(default=True)
    objects = HoursManagement()

    def clean(self):
        def validate_hour():
            try:
                hourValue = Times.objects.filter(
                    diary=self.diary, hour=self.hour).get()
                raise ValidationError({'Agenda já existe'})
            except hourValue.DoesNotExist:
                pass
        validate_hour()

    def __str__(self):
        return f"Agenda {self.diary.id} Horário {self.hour} - {self.diary.day}"
