from rest_framework import generics, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Place, FavoritePlace
from .serializers import (
    PlaceSerializer,
    FavoritePlaceSerializer,
    CreateFavoriteSerializer,
)


# 🔓 View simples e pública: para mostrar em cards no frontend
class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = []  # aberta ao público


# 🔐 Lista os lugares favoritos do usuário autenticado
class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoritePlaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoritePlace.objects.filter(user=self.request.user)


# 🔐 Adiciona um local aos favoritos do usuário autenticado
class FavoriteCreateView(generics.CreateAPIView):
    serializer_class = CreateFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ⚙️ ViewSet com filtros dinâmicos (para painéis e buscas avançadas)
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    # 🔍 Habilita filtros na URL: ?category=, ?search=, ?ordering=
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # 🧩 Filtros exatos (URL)
    filterset_fields = ['category', 'is_accessible', 'supports_local']

    # 🔎 Pesquisa parcial
    search_fields = ['name', 'description']

    # 🔃 Ordenação
    ordering_fields = ['sustainability_score', 'created_at']
