from pydoc import Doc

from diaryDoctor.models import DiaryDoctor, Times
from django.db import models
from doctor.models import Doctor
from patient.models import User


# Create your models here.
class QueryPatient(models.Model):
    diary = models.ForeignKey(DiaryDoctor, on_delete=models.CASCADE)
    hour = models.ForeignKey(Times, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    daySchedule = models.DateField(auto_now_add=True)
