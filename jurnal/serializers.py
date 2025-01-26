from .models import AboutMagazine, MagazineNews, MagazineRequirements, MagazineArchive, MagazineStatistics
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

class MagazineStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineStatistics
        fields = '__all__'

