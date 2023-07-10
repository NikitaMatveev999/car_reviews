from django.http import HttpResponse
from rest_framework import viewsets
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer
from .permissions import CommentPermission
import pandas as pd


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]


def export_data(request, model=None, format=None):
    if model == 'car':
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
    elif model == 'manufacturer':
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
    elif model == 'country':
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
    elif model == 'comment':
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
    else:
        return HttpResponse("Invalid model specified.", status=400)
    if format == 'xlsx':
        df = pd.DataFrame(serializer.data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
        df.to_excel(response, index=False)
        return response
    elif format == 'csv':
        df = pd.DataFrame(serializer.data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        df.to_csv(response, index=False)
        return response
    else:
        return HttpResponse("Invalid format specified.", status=400)
