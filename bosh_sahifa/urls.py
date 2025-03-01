from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MagazineViewSet, ArticleViewSet, ArticleAuthorViewSet, ArticleCategoriesViewSet, upload_file, ConferenceViewSet


router = DefaultRouter()
router.register(r'conferences', ConferenceViewSet)  # /api/conferences/

router.register(r'magazine', MagazineViewSet, basename='magazine')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'article-authors', ArticleAuthorViewSet, basename='article-authors')
router.register(r'article-categories', ArticleCategoriesViewSet, basename='article-categories')

urlpatterns = [
    path('', include(router.urls)),

]
