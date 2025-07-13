from rest_framework import serializers
from .models import Place, Comment, FavoritePlace


# 🌱 Serializer principal para Locais
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            "id",
            "name",
            "category",
            "description",
            "address",
            "latitude",
            "longitude",
            "sustainability_score",
            "is_accessible",
            "supports_local",
            "image",
            "website",
            "phone_number",
            "opening_hours",
            "accessibility_notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


# 💬 Comentários - leitura e criação
class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "place",
            "user",
            "user_name",
            "text",
            "rating",
            "user_location",
            "image",
            "is_verified_visitor",
            "created_at",
        ]
        read_only_fields = ["user", "created_at", "user_name", "is_verified_visitor"]


# ❤️ Favoritos - leitura com detalhes do user e do local
class FavoritePlaceSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)
    place_name = serializers.CharField(source="place.name", read_only=True)

    class Meta:
        model = FavoritePlace
        fields = [
            "id",
            "user",
            "user_name",
            "place",
            "place_name",
            "created_at",
        ]
        read_only_fields = ["user", "created_at"]
        depth = 1  # Exibe detalhes aninhados do Place


# ❤️ Favoritos - criação simplificada (envia só o ID do lugar)
class CreateFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePlace
        fields = ["place"]
