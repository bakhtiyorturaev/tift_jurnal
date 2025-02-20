from .models import Magazine, Article, ArticleAuthor, ArticleCategories
from rest_framework import serializers

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAuthor
        fields = '__all__'

class ArticleCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategories
        fields = '__all__'
