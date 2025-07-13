import { useState, useEffect } from "react";

export default function FavoriteButton({ placeId }) {
  const [isFavorited, setIsFavorited] = useState(false);
  const [loading, setLoading] = useState(true);

  // Busca se o local está favoritado ao carregar
  useEffect(() => {
    fetch("http://localhost:8000/api/user/favorites/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then(res => res.json())
      .then(data => {
        const already = data.some(fav => fav.place.id === placeId);
        setIsFavorited(already);
      })
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, [placeId]);

  const toggleFavorite = async () => {
    try {
      const res = await fetch(`http://localhost:8000/api/places/${placeId}/favorite/`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      const data = await res.json();
      setIsFavorited(data.favorited);
    } catch (err) {
      console.error("Erro ao favoritar:", err);
    }
  };

  if (loading) return null;

  return (
    <button
      onClick={toggleFavorite}
      className={`text-xl transition-colors ${
        isFavorited ? "text-pink-500" : "text-gray-400"
      } hover:scale-110`}
      title={isFavorited ? "Remover dos favoritos" : "Adicionar aos favoritos"}
    >
      ❤️
    </button>
  );
}
