import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <Link to="/" className="text-2xl font-bold text-green-600 dark:text-green-400">
          COP Verde 🌿
        </Link>
        <div className="space-x-6">
          <Link to="/" className="text-gray-800 dark:text-gray-100 hover:text-green-600">
            Início
          </Link>
          <Link to="/places" className="text-gray-800 dark:text-gray-100 hover:text-green-600">
            Locais
          </Link>
          <Link to="/sobre" className="text-gray-800 dark:text-gray-100 hover:text-green-600">
            Sobre
          </Link>
        </div>
      </div>
    </nav>
  );
}
