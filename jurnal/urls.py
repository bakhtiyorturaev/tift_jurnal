from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutMagazineViewSet, MagazineNewsViewSet, MagazineRequirementsViewSet, MagazineArchiveListView, \
    StatisticsViewSet

router = DefaultRouter()
router.register(r'about-magazines', AboutMagazineViewSet, basename='about-magazine')
router.register(r'magazine-news', MagazineNewsViewSet, basename='magazine-news')
router.register(r'journal-requirements', MagazineRequirementsViewSet, basename='journal-requirements')
router.register(r'statistics', StatisticsViewSet, basename='statistics')

urlpatterns = [
    path('', include(router.urls)),
    path('magazine-archives/', MagazineArchiveListView.as_view(), name='magazine-archives'),

]
