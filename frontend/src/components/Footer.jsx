export default function Footer() {
  return (
    <footer className="bg-gray-100 dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700 mt-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 text-center text-sm text-gray-600 dark:text-gray-400">
        <p>
          © {new Date().getFullYear()} COP Verde. Todos os direitos reservados.
        </p>
        <p className="mt-1">
          Feito com ❤️ por <a href="#" className="text-green-600 dark:text-green-400 hover:underline">SoeiroTech</a>
        </p>
      </div>
    </footer>
  );
}
