from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import IlmiyMaktablarim
from .serializers import IlmiyMaktablarimSerializer

class IlmiyMaktablarimViewSet(viewsets.ModelViewSet):
    queryset = IlmiyMaktablarim.objects.all()
    serializer_class = IlmiyMaktablarimSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

