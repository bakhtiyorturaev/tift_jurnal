from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EditorialBoardViewSet, EditorialStaffViewSet, HonoraryForeignEditorialMemberViewSet, \
    ForeignEditorialMemberViewSet

router = DefaultRouter()
router.register(r'editor-board', EditorialBoardViewSet, basename='editor-board')
router.register(r'editor-staff', EditorialStaffViewSet, basename='editor-staff')
router.register(r'honorary-foreign-editorial-members', HonoraryForeignEditorialMemberViewSet, basename='honorary-foreign-editorial-members')
router.register(r'foreign-editorial-members', ForeignEditorialMemberViewSet, basename='foreign-editorial-members')


urlpatterns = [
    path('', include(router.urls)),

]
