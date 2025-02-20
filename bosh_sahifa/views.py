from django.http import FileResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Magazine, Article, ArticleAuthor, ArticleCategories
from .serializers import MagazineSerializer, ArticleSerializer, ArticleAuthorSerializer, ArticleCategoriesSerializer
from rest_framework.response import Response

class MagazineViewSet(ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], url_path='slug/(?P<slug>[^/.]+)')
    def get_by_slug(self, request, slug=None):
        magazine = get_object_or_404(Magazine, slug=slug)
        serializer = self.get_serializer(magazine)
        return Response(serializer.data)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def view_article_or_download(self, pk):
        article = get_object_or_404(Article, pk=pk)
        pdf_file = article.pdf_file

        response = FileResponse(pdf_file)
        response['Content-Disposition'] = f'inline; filename={article.title}.pdf'
        return response

class ArticleAuthorViewSet(ModelViewSet):
    queryset = ArticleAuthor.objects.all()
    serializer_class = ArticleAuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleCategoriesViewSet(ModelViewSet):
    queryset = ArticleCategories.objects.all()
    serializer_class = ArticleCategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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