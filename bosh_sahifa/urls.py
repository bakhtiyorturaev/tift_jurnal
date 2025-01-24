from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MagazineViewSet, ArticleViewSet, ArticleAuthorViewSet, ArticleCategoriesViewSet, upload_file

router = DefaultRouter()
router.register('magazines', MagazineViewSet)
router.register('articles', ArticleViewSet)
router.register('article-authors', ArticleAuthorViewSet)
router.register('article-categories', ArticleCategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("upload_magazine_file/", upload_file, name="ck_editor_5_upload_file"),

]
