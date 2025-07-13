import { useEffect, useState } from "react";

export default function CommentSection({ placeId }) {
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState({
    text: "",
    rating: 5,
    user_location: "",
    image: null,
  });
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:8000/api/places/${placeId}/comments/`)
      .then(res => res.json())
      .then(data => setComments(data))
      .catch(err => setErro("Erro ao carregar comentários"))
      .finally(() => setLoading(false));
  }, [placeId]);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (name === "image") {
      setNewComment({ ...newComment, image: files[0] });
    } else {
      setNewComment({ ...newComment, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);

    const formData = new FormData();
    Object.entries(newComment).forEach(([key, value]) => {
      if (value) formData.append(key, value);
    });

    try {
      const res = await fetch(`http://localhost:8000/api/places/${placeId}/comments/`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`, // ajuste conforme seu auth
        },
        body: formData,
      });

      if (!res.ok) throw new Error("Erro ao enviar comentário");
      const data = await res.json();
      setComments([data, ...comments]);
      setNewComment({ text: "", rating: 5, user_location: "", image: null });
    } catch (err) {
      alert(err.message);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="mt-10">
      <h2 className="text-xl font-bold mb-4">💬 Comentários</h2>

      {loading ? (
        <p className="animate-pulse">⏳ Carregando...</p>
      ) : erro ? (
        <p className="text-red-500">{erro}</p>
      ) : comments.length === 0 ? (
        <p className="text-gray-600">Nenhum comentário ainda.</p>
      ) : (
        <ul className="space-y-4 mb-8">
          {comments.map((c) => (
            <li key={c.id} className="border border-gray-200 dark:border-gray-700 rounded-lg p-4">
              <div className="flex items-center justify-between mb-1">
                <strong>{c.user_name}</strong>
                <span className="text-sm text-yellow-600">⭐ {c.rating}/10</span>
              </div>
              {c.user_location && <p className="text-xs text-gray-500">📍 {c.user_location}</p>}
              <p className="text-sm mt-2">{c.text}</p>
              {c.image && (
                <img
                  src={c.image}
                  alt="Comentário"
                  className="mt-2 w-full max-w-xs rounded shadow-md"
                />
              )}
            </li>
          ))}
        </ul>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          name="text"
          value={newComment.text}
          onChange={handleChange}
          rows={3}
          placeholder="Escreva seu comentário..."
          required
          className="w-full border rounded p-2 dark:bg-gray-800 dark:text-white"
        />

        <div className="flex gap-4 items-center">
          <label className="text-sm">⭐ Nota:
            <input
              type="number"
              name="rating"
              value={newComment.rating}
              onChange={handleChange}
              min={1}
              max={10}
              className="ml-2 w-16 text-center border rounded dark:bg-gray-800"
            />
          </label>

          <input
            type="text"
            name="user_location"
            value={newComment.user_location}
            onChange={handleChange}
            placeholder="Sua cidade/estado"
            className="flex-1 border rounded p-1 dark:bg-gray-800 dark:text-white"
          />

          <input
            type="file"
            name="image"
            accept="image/*"
            onChange={handleChange}
            className="text-sm"
          />
        </div>

        <button
          type="submit"
          disabled={submitting}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {submitting ? "Enviando..." : "Enviar comentário"}
        </button>
      </form>
    </div>
  );
}
