import { useEffect, useState } from "react";
import axios from "axios";
import PlaceCard from "../components/PlaceCard";

export default function Home() {
  const [places, setPlaces] = useState([]);
  const [erro, setErro] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/v1/places/")
      .then((res) => setPlaces(res.data))
      .catch(() => setErro("Erro ao carregar os dados."))
      .finally(() => setLoading(false));
  }, []);

  return (
    <main className="max-w-6xl mx-auto px-4 py-8">
      {/* Cabeçalho */}
      <header className="mb-8" aria-labelledby="titulo">
        <h1 id="titulo" className="text-3xl font-bold text-green-700 dark:text-green-400 mb-1">
          🌱 COP Verde – Locais Sustentáveis
        </h1>
        <p className="text-gray-600 dark:text-gray-300 text-sm sm:text-base">
          Descubra os pontos sustentáveis de Belém e viva a cidade de forma consciente.
        </p>
      </header>

      {/* Estado de carregamento */}
      {loading && (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {Array.from({ length: 6 }).map((_, index) => (
            <div
              key={index}
              className="h-56 bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse"
            />
          ))}
        </div>
      )}

      {/* Estado de erro */}
      {!loading && erro && (
        <div className="text-center text-red-500 font-medium animate-pulse">
          ❌ {erro}
        </div>
      )}

      {/* Lista de locais */}
      {!loading && !erro && (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {places.map((place) => (
            <PlaceCard key={place.id} place={place} />
          ))}
        </div>
      )}
    </main>
  );
}
