from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember
from .serializers import EditorialStaffSerializer, HonoraryForeignEditorialMemberSerializer, \
    ForeignEditorialMemberSerializer

class EditorialStaffViewSet(viewsets.ModelViewSet):
    queryset = EditorialStaff.objects.all()
    serializer_class = EditorialStaffSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HonoraryForeignEditorialMemberViewSet(viewsets.ModelViewSet):
    queryset = HonoraryForeignEditorialMember.objects.all()
    serializer_class = HonoraryForeignEditorialMemberSerializer

class ForeignEditorialMemberViewSet(viewsets.ModelViewSet):
    queryset = ForeignEditorialMember.objects.all()
    serializer_class = ForeignEditorialMemberSerializer
