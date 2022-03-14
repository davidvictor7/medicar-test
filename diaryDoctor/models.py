from django.db import models
from django.utils import timezone
from doctor.models import Doctor
from pyexpat import model


# Create your models here.
class DiaryDoctor(models.Model):
    day = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    freeDay = models.BooleanField(default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agenda {self.id} - {self.day} / Medico: {self.doctor}"


class Times(models.Model):
    diary = models.ForeignKey(
        DiaryDoctor, related_name='hours', on_delete=True)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    freeHour = models.BooleanField(default=True)

    def __str__(self):
        return f"Agenda {self.diary.id} Horário {self.hour} - {self.diary.day}"
