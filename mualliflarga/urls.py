from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticlePreparationViewSet, SampleDocumentViewSet, CopyRightViewSet

router = DefaultRouter()
router.register(r'article-preparation-guides', ArticlePreparationViewSet, basename='article-preparation-guides')
router.register(r'sample-documents', SampleDocumentViewSet, basename='sample-documents')
router.register(r'copyright', CopyRightViewSet, basename='copyright')

urlpatterns = [
    path('', include(router.urls)),

]
