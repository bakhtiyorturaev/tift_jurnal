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


class ArticleSerializer(serializers.ModelSerializer):
    view_article_or_download = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ["id", "name_uz", "upload_file_uz", "view_article_or_download"]

    def get_view_article_or_download(self, obj):
        """
        Maqolani yuklab olish yoki ko‘rish URL'sini yaratish.
        """
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(reverse('article-view-article-or-download', args=[obj.pk]))
        return None

class ArticleCategoriesSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(source='article_set', many=True, read_only=True)  # ✅ Kategoriya ichidagi maqolalar

    class Meta:
        model = ArticleCategories
        fields = ["id", "name_uz", "name_ru", "name_en", "magazine", "articles"]


