from .models import Magazine, Article, ArticleAuthor, ArticleCategories, Conference
from rest_framework import serializers
##
class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = "__all__"
##
class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAuthor
        fields = '__all__'

class ArticleCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategories
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    magazine = MagazineSerializer(read_only=True)  # Nested serializer
    category = ArticleCategoriesSerializer(read_only=True)  # Nested serializer
    author = ArticleAuthorSerializer(read_only=True)  # Nested serializer


    class Meta:
        model = Article
        fields = '__all__'
