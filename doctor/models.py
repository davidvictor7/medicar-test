from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    crm = models.IntegerField(unique=True)
    mail = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Medico: {self.name} - CRM: {self.crm}"
