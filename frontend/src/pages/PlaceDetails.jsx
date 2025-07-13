import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import CategoryTag from "../components/CategoryTag";
import CommentSection from "../components/CommentSection";
import FavoriteButton from "../components/FavoriteButton";

export default function PlaceDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [place, setPlace] = useState(null);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    const fetchPlace = async () => {
      try {
        const res = await fetch(`http://localhost:8000/api/v1/places/${id}/`);
        if (!res.ok) throw new Error("Erro ao buscar local.");
        const data = await res.json();
        setPlace(data);
      } catch (err) {
        setErro(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPlace();
  }, [id]);

  if (loading)
    return <p className="text-center mt-10 animate-pulse">⏳ Carregando...</p>;

  if (erro)
    return (
      <p className="text-center mt-10 text-red-600 font-medium">
        ❌ {erro}
      </p>
    );

  if (!place)
    return (
      <p className="text-center mt-10 text-gray-600">
        ❌ Local não encontrado.
      </p>
    );

  return (
    <main className="max-w-4xl mx-auto px-4 py-6">
      {/* Botão de voltar */}
      <button
        onClick={() => navigate(-1)}
        className="inline-flex items-center gap-1 text-blue-600 hover:text-blue-800 font-semibold mb-6"
      >
        <span className="text-lg">←</span> Voltar
      </button>

      {/* Imagem principal */}
      {place.image && (
        <img
          src={place.image}
          alt={`Imagem de ${place.name}`}
          className="w-full h-80 object-cover rounded-xl shadow-lg mb-6"
        />
      )}

      {/* Título + categoria + favorito */}
      <header className="flex items-start justify-between mb-4">
        <div>
          <h1 className="text-3xl font-bold">{place.name}</h1>
          <div className="mt-2">
            <CategoryTag category={place.category} />
          </div>
        </div>
        <FavoriteButton placeId={place.id} />
      </header>

      {/* Descrição */}
      <section className="mb-6 leading-relaxed">
        <p className="text-base text-gray-800 dark:text-gray-200">
          {place.description}
        </p>
      </section>

      {/* Informações detalhadas */}
      <section className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm text-gray-800 dark:text-gray-200">
        <p><strong>📍 Endereço:</strong> {place.address}</p>
        <p><strong>🌎 Latitude:</strong> {place.latitude}</p>
        <p><strong>🌍 Longitude:</strong> {place.longitude}</p>
        <p className="flex items-center gap-2">
          <strong>♻️ Sustentabilidade:</strong>
          <span className={`font-bold ${place.sustainability_score >= 7 ? "text-green-600" : "text-yellow-600"}`}>
            {place.sustainability_score}/10
          </span>
        </p>
        <p className="flex items-center gap-2">
          <strong>🧑‍🦽 Acessível:</strong>
          {place.is_accessible ? (
            <span className="text-green-700 font-medium">Sim ✅</span>
          ) : (
            <span className="text-red-500 font-medium">Não ❌</span>
          )}
        </p>
      </section>

      {/* Google Maps */}
      {place.latitude && place.longitude && (
        <a
          href={`https://www.google.com/maps?q=${place.latitude},${place.longitude}`}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-6 inline-block text-sm text-green-600 hover:underline"
        >
          📌 Ver no Google Maps
        </a>
      )}

      {/* Comentários */}
      <div className="mt-10">
        <CommentSection placeId={place.id} />
      </div>
    </main>
  );
}
