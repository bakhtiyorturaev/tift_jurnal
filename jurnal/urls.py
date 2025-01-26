from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutMagazineViewSet, MagazineNewsViewSet, MagazineRequirementsViewSet, MagazineArchiveListView, \
    MagazineStatisticsListView

router = DefaultRouter()
router.register(r'about-magazines', AboutMagazineViewSet, basename='about-magazine')
router.register(r'magazine-news', MagazineNewsViewSet, basename='magazine-news')
router.register(r'journal-requirements', MagazineRequirementsViewSet, basename='journal-requirements')

urlpatterns = [
    path('', include(router.urls)),
    path('magazine-archives/', MagazineArchiveListView.as_view(), name='magazine-archives'),
    path('magazine-statistics/', MagazineStatisticsListView.as_view(), name='magazine-statistics'),

]
