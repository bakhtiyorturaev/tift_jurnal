from django.urls import reverse
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
    view_article_or_download = serializers.SerializerMethodField()  # Custom field

    class Meta:
        model = Article
        fields = ["name_uz", "upload_file_uz", "magazine", "category", "author", "view_article_or_download"]

    def get_view_article_or_download(self, obj):
        """
        Har bir maqola uchun yuklab olish yoki ko'rish URL'sini yaratadi.
        """
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(reverse('article-view-article-or-download', args=[obj.pk]))
        return None

    class Meta:
        model = Article
        fields = '__all__'
