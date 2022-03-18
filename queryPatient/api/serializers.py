from datetime import datetime

from diaryDoctor.api.serializers import TimesSerializer
from diaryDoctor.models import DiaryDoctor, Times
from doctor.api.serializers import DoctorSerializer
from patient.models import User
from queryPatient.models import QueryPatient
from rest_framework import serializers


class DiaryDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryDoctor
        fields = ['day']


class QueryPatientSerializer(serializers.ModelSerializer):
    diary = DiaryDaySerializer()
    hour = TimesSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = QueryPatient
        fields = ['id', 'diary', 'hour', 'daySchedule', 'doctor']


class queryDestroySerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def validate(self, data):
        realTime = datetime.now().time()
        query = QueryPatient.objects.get(pk=data['id'])
        return data


class querySetSerializer(serializers.Serializer):
    idQuery = serializers.IntegerField()
    hour = serializers.TimeField()

    def validate(self, data):
        def validate_diary(data):
            diary = DiaryDoctor.objects.get(id=data['idQuery'])

        def validate_hour(data):
            hours = Times.objects.get(
                diary_id=data['idQuery'], hour=data['hour'])

        validate_diary(data)
        validate_hour(data)
        return data

    def save(self):
        idDiary = self.validated_data['idQuery']
        hourRequire = self.validated_data['hour']

        diary = DiaryDoctor.objects.get(id=idDiary)
        doctor = DiaryDoctor.doctor
        patient = User.objects.get(username=self.context['request'].user)
        hours = Times.objects.get(diary_id=idDiary, hora=hourRequire)

        query = QueryPatient(diary=diary, hour=hours,
                             doctor=doctor, patient=patient)
        updateHour = Times.objects.filter(pk=hours.id).update(freeHour=False)

        query.save()
        return query
