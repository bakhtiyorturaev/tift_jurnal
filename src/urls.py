from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Tift Jurnal API",
        default_version='v1',
        description="Tift uchun Jurnal va maqolalar sayti.",
        terms_of_service=" ",
        contact=openapi.Contact(email="baxti.dev1@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path(settings.SECRET_ADMIN_URL, admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Barcha app URL-lari uchun til kodi boshida ko‘rsatiladi
urlpatterns += i18n_patterns(
    path('', include('bosh_sahifa.urls')),
    path('ilmiy/', include('ilmiy_maktablarim.urls')),
    path('contacts/', include('contacts.urls')),
    path('jurnal/', include('jurnal.urls')),
    path('muallif/', include('mualliflarga.urls')),
    path('tahririyat/', include('tahririyat.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
