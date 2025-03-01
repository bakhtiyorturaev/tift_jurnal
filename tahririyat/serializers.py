from rest_framework import serializers
from .models import EditorialStaff, HonoraryForeignEditorialMember, ForeignEditorialMember


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

