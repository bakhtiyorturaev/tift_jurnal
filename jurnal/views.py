from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import AboutMagazine, MagazineNews, MagazineRequirements, MagazineArchive, Statistics
from .serializers import AboutMagazineSerializer, MagazineNewsSerializer, MagazineRequirementsSerializer, \
    MagazineArchiveSerializer, StatisticsSerializer

class AboutMagazineViewSet(viewsets.ModelViewSet):
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

class MagazineArchiveViewSet(viewsets.ModelViewSet):
    queryset = MagazineArchive.objects.all().order_by('-id')  # So'nggi yozuvlar birinchi
    serializer_class = MagazineArchiveSerializer
    pagination_class = MagazinePagination
    permission_classes = [IsAuthenticatedOrReadOnly]

class StatisticsViewSet(ReadOnlyModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
