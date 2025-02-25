# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.files.storage import default_storage
from django.conf import settings

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        image = request.FILES.get('file')
        if image:
            path = default_storage.save(f"tinymce_file/{image.name}", image)
            image_url = f"{settings.MEDIA_URL}{path}"
            return Response({'location': image_url}, status=200)
        return Response({'error': 'Fayl topilmadi'}, status=400)
