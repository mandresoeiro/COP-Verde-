from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # 🔐 Autenticação (login, logout, senha, etc)
    path("api/auth/", include("dj_rest_auth.urls")),

    # 🆕 Registro de usuários
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),

    # 👤 Perfil de usuário logado (accounts app)
    path("api/accounts/", include("apps.accounts.urls")),

    # 🌱 API REST padrão via ViewSet (DRF Router)
    # Deve estar assim:
path('api/v1/', include('apps.places.urls')),  # <- isso inclui PlaceViewSet com router


    # 💬 Endpoints adicionais (comentários, favoritos, etc.)
    path("api/", include(("apps.places.api_urls", "places_api"), namespace="places_api")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
