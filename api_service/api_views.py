from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Avg, F
from rest_framework import status

from .models import BirthDay
from .filters import BirthdayDateFilter
from .serializers import BirthdayModelSerializer
from .utils import convert_day_to_year, lower_and_upper_variations


class BirthdayModelViewSet(viewsets.ModelViewSet):
    serializer_class = BirthdayModelSerializer
    queryset = BirthDay.objects.all()
    filterset_class = BirthdayDateFilter

    def create(self, request):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            birthday = serializer.save()
            return Response({
                'data' : self.serializer_class(birthday, many=True).data,
            }, status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False, url_path='get-average-age',
        url_name='average_age')
    def get_average_age(self, request):
        qs = BirthDay.objects.get_average_age()
        response = convert_day_to_year(qs['average_age'])
        return Response({
            "average_age" : response
        }, status.HTTP_200_OK)


class LetterDigitAPIView(APIView):
    def get(self, request, string):
        result = lower_and_upper_variations(string)
        return Response({
            'result' : result
        }, status.HTTP_200_OK)
