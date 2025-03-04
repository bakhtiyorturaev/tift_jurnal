from django.http import FileResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Magazine, Article, ArticleAuthor, ArticleCategories
from .serializers import MagazineSerializer, ArticleSerializer, ArticleAuthorSerializer, ArticleCategoriesSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Conference
from .serializers import ConferenceSerializer

class ConferenceViewSet(ReadOnlyModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

##
class MagazineViewSet(ReadOnlyModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'], url_path='articles')
    def get_articles(self, request, pk=None):
        """
        Berilgan `magazine_id` bo‘yicha maqolalar va ularning kategoriyalarini olish.
        """
        articles = Article.objects.filter(magazine_id=pk).select_related("category", "author")
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        return Response(serializer.data)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def view_article_or_download(self, request, pk=None):
        """
        Maqolani ko'rish yoki PDF faylni yuklab olish uchun funksiya.
        """
        article = get_object_or_404(Article, pk=pk)
        pdf_file = article.upload_file_uz  # Modeldagi fayl maydoni

        response = FileResponse(pdf_file)
        response['Content-Disposition'] = f'inline; filename="{article.name_uz}.pdf"'
        return response

class ArticleAuthorViewSet(ReadOnlyModelViewSet):
    queryset = ArticleAuthor.objects.all()
    serializer_class = ArticleAuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleCategoriesViewSet(ReadOnlyModelViewSet):
    """
    Maqola kategoriyalari va ularning ichidagi maqolalar ro‘yxati.
    """
    queryset = ArticleCategories.objects.prefetch_related("article_set__author")
    serializer_class = ArticleCategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], url_path='by-magazine/(?P<magazine_id>\d+)')
    def get_by_magazine(self, request, magazine_id=None):
        """
        Berilgan `magazine_id` bo‘yicha jurnal ma'lumotlari, kategoriyalar va maqolalarni olish.
        """
        magazine = get_object_or_404(Magazine, id=magazine_id)  # Jurnalni olish
        categories = ArticleCategories.objects.filter(magazine_id=magazine_id).prefetch_related("article_set__author")

        magazine_serializer = MagazineSerializer(magazine)
        category_serializer = ArticleCategoriesSerializer(categories, many=True, context={'request': request})

        return Response({
            "magazine": magazine_serializer.data,  # Jurnal haqida ma'lumot
            "categories": category_serializer.data  # Jurnalga tegishli kategoriyalar va maqolalar
        })

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('upload')  # Yuklangan fayl
        if file:
            fs = FileSystemStorage(location='jurnal/bio_files/')  # Fayllarni saqlash uchun katalog belgilash
            filename = fs.save(file.name, file)  # Faylni saqlash
            file_url = fs.url(filename)  # Fayl uchun URL olish
            return JsonResponse({"uploaded": True, "url": file_url})
        else:
            return JsonResponse({"uploaded": False, "error": "No file uploaded"})

    return JsonResponse({"uploaded": False, "error": "Invalid request method"})
