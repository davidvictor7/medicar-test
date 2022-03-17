from diaryDoctor.api.serializers import TimesSerializer
from diaryDoctor.models import DiaryDoctor, Times
from doctor.api.serializers import DoctorSerializer
from queryPatient.models import QueryPatient
from rest_framework.serializers import ModelSerializer


class DiaryDaySerializer(ModelSerializer):
    class Meta:
        model = DiaryDoctor
        fields = ['day']


class QueryPatientSerializer(ModelSerializer):
    diary = DiaryDaySerializer()
    hour = TimesSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = QueryPatient
        fields = ['id', 'diary', 'hour', 'daySchedule', 'doctor']
