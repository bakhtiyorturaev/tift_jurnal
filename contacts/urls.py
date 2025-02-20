from django.urls import path, include
from .views import ContactsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]