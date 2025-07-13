import { Link } from "react-router-dom";
import CategoryTag from "../components/CategoryTag";

export default function PlaceCard({ place }) {
  return (
    <Link
      to={`/places/${place.id}`}
      className="block transition-transform duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-500 rounded-2xl"
      aria-label={`Ver detalhes do local: ${place.name}`}
    >
      <div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-white 
                      rounded-2xl shadow-lg overflow-hidden 
                      border-l-4 border-green-500 flex flex-col h-full 
                      transition-colors duration-300 hover:bg-gray-50 dark:hover:bg-gray-800">
        
        {/* Imagem do local */}
        {place.image && (
          <img
            src={place.image}
            alt={`Imagem de ${place.name}`}
            className="w-full h-44 object-cover"
            loading="lazy"
          />
        )}

        {/* Conteúdo do card */}
        <div className="p-5 flex flex-col justify-between flex-grow">
          <div>
            <h2 className="text-xl font-bold mb-2 leading-snug">
              {place.name}
            </h2>
            <CategoryTag category={place.category} />
            <p className="text-sm mt-3 text-gray-900 dark:text-gray-100 font-medium leading-relaxed line-clamp-2">
              {place.description}
            </p>
          </div>
        </div>
      </div>
    </Link>
  );
}
