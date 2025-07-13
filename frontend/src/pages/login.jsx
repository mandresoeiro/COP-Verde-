import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function Login() {
  const { login } = useContext(AuthContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [erro, setErro] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:8000/api/auth/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Login inválido");
        return res.json();
      })
      .then((data) => {
        login(data.key); // salva token no contexto
      })
      .catch((err) => setErro(err.message));
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-10 space-y-4">
      <h2 className="text-xl font-bold">Entrar</h2>
      {erro && <p className="text-red-500">{erro}</p>}
      <input
        type="text"
        placeholder="Usuário"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        className="w-full p-2 border rounded"
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full p-2 border rounded"
      />
      <button className="bg-blue-600 text-white px-4 py-2 rounded">
        Entrar
      </button>
    </form>
  );
}
