from .models import AboutMagazine, MagazineNews, MagazineRequirements, MagazineArchive, Statistics
from rest_framework import serializers


class AboutMagazineSerializer(serializers.ModelSerializer):
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

class MagazineArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineArchive
        fields = '__all__'

class StatisticsSerializer(serializers.ModelSerializer):
    magazine_info = serializers.CharField(source='magazine_info', read_only=True)
    articles_count = serializers.IntegerField(source='articles_count', read_only=True)

    class Meta:
        model = Statistics
        fields = ['id', 'magazine', 'magazine_info', 'articles_count']
