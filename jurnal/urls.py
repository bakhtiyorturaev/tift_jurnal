from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutMagazineViewSet, MagazineNewsViewSet, MagazineRequirementsViewSet, \
    StatisticsViewSet, MagazineArchiveViewSet

router = DefaultRouter()
router.register(r'about-magazines', AboutMagazineViewSet, basename='about-magazine')
router.register(r'magazine-news', MagazineNewsViewSet, basename='magazine-news')
router.register(r'journal-requirements', MagazineRequirementsViewSet, basename='journal-requirements')
router.register(r'statistics', StatisticsViewSet, basename='statistics')
router.register(r'magazine-archives', MagazineArchiveViewSet, basename='magazine-archive')

urlpatterns = [
    path('', include(router.urls)),


]
