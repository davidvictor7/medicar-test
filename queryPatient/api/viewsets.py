
from urllib import response

from diaryDoctor.models import Times
from queryPatient.api.serializers import (QueryPatientSerializer,
                                          queryDestroySerializer,
                                          querySetSerializer)
from queryPatient.models import QueryPatient
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class QueryPatientViewSet(ViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = QueryPatient.objects.all()
    # serializer_class = QueryPatientSerializer

    def destroy(self, request, pk):

        data = {}
        data['id'] = pk

        serializerDestroy = queryDestroySerializer(data=data)
        serializerDestroy.is_valid(raise_exception=True)

        query = QueryPatient.objects.get(pk=data['id'])
        unchecked = Times.objects.filter(
            pk=query.hour.id).update(freeHour=True)
        query.delete()

        return Response({})

    def list(self, request):
        queryset = QueryPatient.objects.all()
        serializerList = QueryPatientSerializer(queryset, many=True)

        return Response(serializerList.data)

    def create(self, request):
        serializer = querySetSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
