from .models import AboutMagazine, MagazineNews, MagazineRequirements, Statistics
from rest_framework import serializers
from bosh_sahifa.serializers import MagazineSerializer


class AboutMagazineSerializer(serializers.ModelSerializer):
    magazine = MagazineSerializer()
    class Meta:
        model = AboutMagazine
        fields = '__all__'


class MagazineNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineNews
        fields = '__all__'

class MagazineRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineRequirements
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    magazine_info = serializers.CharField(read_only=True)
    articles_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Statistics
        fields = ['id', 'magazine', 'magazine_info', 'articles_count']
