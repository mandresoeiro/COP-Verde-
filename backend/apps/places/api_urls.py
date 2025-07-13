from django.urls import path
from .views_api import (
    CommentListCreateView,
    ToggleFavoriteView,
    FavoriteListView,
)

app_name = "places_api"

urlpatterns = [
    # 💬 Comentários por local
    path("places/<int:place_id>/comments/", CommentListCreateView.as_view(), name="place-comments"),

    # ❤️ Favoritar/desfavoritar local (toggle)
    path("places/<int:place_id>/favorite/", ToggleFavoriteView.as_view(), name="toggle-favorite"),

    # ❤️ Listar favoritos do usuário
    path("user/favorites/", FavoriteListView.as_view(), name="user-favorites"),
]
