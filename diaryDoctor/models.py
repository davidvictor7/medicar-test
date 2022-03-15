from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from doctor.models import Doctor


# Create your models here.
class DiaryDoctor(models.Model):
    day = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    freeDay = models.BooleanField(default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def clean_date(self):
        def validate_day():
            if self.day < date.today():
                raise ValidationError({"A data não pode ser anterior a hoje!"})
            return self.day

        validate_day()

    def __str__(self):
        return f"Agenda {self.id} - {self.day} / Medico: {self.doctor}"


class Times(models.Model):
    diary = models.ForeignKey(
        DiaryDoctor, related_name='hours', on_delete=models.CASCADE)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    freeHour = models.BooleanField(default=True)

    def __str__(self):
        return f"Agenda {self.diary.id} Horário {self.hour} - {self.diary.day}"
