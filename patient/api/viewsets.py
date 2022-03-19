
from patient.api.serializers import PatientSerializer
from patient.models import User
from rest_framework.views import APIView


class PatientViewset(APIView):
    queryset = User.objects.all()
    serializer_class = PatientSerializer
