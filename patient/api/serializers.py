from patient.models import User
from rest_framework.serializers import ModelSerializer


class PatientSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
