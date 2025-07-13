from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Comment, FavoritePlace, Place
from .serializers import (
    CommentSerializer,
    FavoritePlaceSerializer,
    CreateFavoriteSerializer,
)


# 💬 Comentários: listar e criar
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(place_id=self.kwargs["place_id"]).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, place_id=self.kwargs["place_id"])


# ❤️ Favoritar/desfavoritar um local (toggle)
class ToggleFavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, place_id):
        place = get_object_or_404(Place, id=place_id)
        favorite, created = FavoritePlace.objects.get_or_create(user=request.user, place=place)

        if not created:
            favorite.delete()
            return Response({"favorited": False}, status=status.HTTP_200_OK)

        return Response({"favorited": True}, status=status.HTTP_201_CREATED)


# ❤️ Listar locais favoritados pelo usuário logado
class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoritePlaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoritePlace.objects.filter(user=self.request.user).order_by("-created_at")
