from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ArticlePreparationGuide, SampleDoc, CopyRight
from .serializers import ArticlePreparationGuideSerializer, SampleDocsSerializer, CopyRightSerializer


class ArticlePreparationViewSet(viewsets.ViewSet):
    queryset = ArticlePreparationGuide.objects.all()
    serializer_class = ArticlePreparationGuideSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SampleDocumentViewSet(viewsets.ViewSet):
    queryset = SampleDoc.objects.all()
    serializer_class = SampleDocsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CopyRightViewSet(viewsets.ViewSet):
    queryset = CopyRight.objects.all()
    serializer_class = CopyRightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
