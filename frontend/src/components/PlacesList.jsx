// frontend/src/components/PlacesList.jsx
import React, { useEffect, useState } from "react";
import PlaceCard from "./PlaceCard";

const API_URL = "http://localhost:8000/api/v1/places/";

export default function PlacesList() {
  const [places, setPlaces] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    const fetchPlaces = async () => {
      try {
        const response = await fetch(API_URL);

        if (!response.ok) {
          throw new Error("Erro ao carregar os dados dos locais.");
        }

        const data = await response.json();
        setPlaces(data);
      } catch (err) {
        console.error("Erro na requisição:", err);
        setErro(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPlaces();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center py-10">
  <div className="flex items-center space-x-3 animate-pulse">
    <span className="text-2xl">⏳</span>
    <span className="text-gray-700 dark:text-gray-300 text-lg font-medium">
      Carregando locais...
    </span>
  </div>
</div>


    );
  }

  if (erro) {
    return (
      <div className="text-center text-red-500 py-6">
        ❌ Ocorreu um erro: {erro}
      </div>
    );
  }

  if (places.length === 0) {
    return (
      <div className="text-center text-gray-400 py-6">
        📭 Nenhum local encontrado.
      </div>
    );
  }

  return (
    <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 p-4">
      {places.map((place) => (
        <PlaceCard key={place.id} place={place} />
      ))}
    </div>
  );
}
