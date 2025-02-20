from rest_framework import serializers
from .models import IlmiyMaktablarim

class IlmiyMaktablarimSerializer(serializers.ModelSerializer):
    class Meta:
        model = IlmiyMaktablarim
        fields = '__all__'
