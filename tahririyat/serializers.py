from rest_framework import serializers
from .models import EditorialMember, EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember


class EditorialBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorialMember
        fields = '__all__'


class EditorialStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorialStaff
        fields = '__all__'

class HonoraryForeignEditorialMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HonoraryForeignEditorialMember
        fields = '__all__'

# Xorijiy Tahririyat Azolari uchun Serializer
class ForeignEditorialMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEditorialMember
        fields = '__all__'

