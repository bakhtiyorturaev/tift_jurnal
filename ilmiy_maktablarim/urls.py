from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IlmiyMaktablarimViewSet

router = DefaultRouter()
router.register(r'ilmiy-maktablarim', IlmiyMaktablarimViewSet, basename='ilmiy-maktablarim')

urlpatterns = [
    path('', include(router.urls)),
]
