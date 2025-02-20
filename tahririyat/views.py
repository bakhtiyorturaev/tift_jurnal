from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import EditorialMember, EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember
from .serializers import EditorialBoardSerializer, EditorialStaffSerializer, HonoraryForeignEditorialMemberSerializer, \
    ForeignEditorialMemberSerializer


class EditorialBoardViewSet(viewsets.ModelViewSet):
    queryset = EditorialMember.objects.all()
    serializer_class = EditorialBoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
