from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import AboutMagazine, MagazineNews, MagazineRequirements, Statistics
from .serializers import AboutMagazineSerializer, MagazineNewsSerializer, MagazineRequirementsSerializer, \
     StatisticsSerializer

class AboutMagazineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutMagazine.objects.all()
    serializer_class = AboutMagazineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MagazineNewsViewSet(viewsets.ModelViewSet):
    queryset = MagazineNews.objects.all()
    serializer_class = MagazineNewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MagazineRequirementsViewSet(viewsets.ModelViewSet):
    queryset = MagazineRequirements.objects.all()
    serializer_class = MagazineRequirementsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MagazinePagination(PageNumberPagination):
    page_size = 10  # Har bir sahifada 10 ta yozuv bo'ladi
    page_size_query_param = 'page_size'
    max_page_size = 20  # Maksimal sahifa hajmi

class StatisticsViewSet(ReadOnlyModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
