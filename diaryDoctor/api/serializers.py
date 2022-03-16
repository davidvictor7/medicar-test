from diaryDoctor.models import DiaryDoctor, Times
from doctor.api.serializers import DoctorSerializer
from rest_framework.serializers import ModelSerializer


class TimesSerializer(ModelSerializer):
    class Meta:
        model = Times
        fields = ['hour']


class DiaryDoctorSerializer(ModelSerializer):
    doctor = DoctorSerializer()
    hours = TimesSerializer(many=True)

    class Meta:
        model = DiaryDoctor
        fields = ['id', 'doctor', 'day', 'hours']
