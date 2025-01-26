from rest_framework import serializers

from .models import ArticlePreparationGuide, SampleDoc, CopyRight


class ArticlePreparationGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePreparationGuide
        fields = '__all__'

class SampleDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleDoc
        fields = '__all__'

class CopyRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyRight
        fields = '__all__'
