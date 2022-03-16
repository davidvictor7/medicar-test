from doctor.models import Doctor
from rest_framework.serializers import ModelSerializer


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'crm', 'mail']
