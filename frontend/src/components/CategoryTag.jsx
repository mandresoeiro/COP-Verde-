// frontend/src/components/CategoryTag.jsx

import {
  MapPin,
  Utensils,
  TreePalm,
  Landmark,
  HelpCircle
} from 'lucide-react';

const categoryMap = {
  ponto_turistico: {
    label: 'Turismo',
    icon: Landmark,
    color: 'bg-blue-100 text-blue-700'
  },
  restaurante: {
    label: 'Restaurante',
    icon: Utensils,
    color: 'bg-red-100 text-red-700'
  },
  espaco_verde: {
    label: 'Espaço Verde',
    icon: TreePalm,
    color: 'bg-green-100 text-green-700'
  },
  cultura: {
    label: 'Cultura',
    icon: MapPin,
    color: 'bg-purple-100 text-purple-700'
  },
  outros: {
    label: 'Outros',
    icon: HelpCircle,
    color: 'bg-gray-100 text-gray-700'
  }
};

export default function CategoryTag({ category }) {
  const { label, icon: Icon, color } = categoryMap[category] || categoryMap['outros'];

  return (
    <span
      className={`inline-flex items-center gap-1 px-2 py-1 rounded-full text-sm font-medium ${color}`}
      aria-label={`Categoria: ${label}`}
    >
      <Icon size={16} />
      {label}
    </span>
  );
}
