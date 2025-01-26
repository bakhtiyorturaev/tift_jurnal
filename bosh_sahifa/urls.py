from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MagazineViewSet, ArticleViewSet, ArticleAuthorViewSet, ArticleCategoriesViewSet, upload_file

router = DefaultRouter()
router.register(r'magazine', MagazineViewSet, basename='magazine')
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'article-authors', ArticleAuthorViewSet, basename='article-authors')
router.register(r'article-categories', ArticleCategoriesViewSet, basename='article-categories')

urlpatterns = [
    path("upload_magazine_file/", upload_file, name="ck_editor_5_upload_file"),
    path('', include(router.urls)),

]
