import { createContext, useState, useEffect } from "react";

export const AuthContext = createContext();

export default function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("token") || null);

  useEffect(() => {
    if (token) {
      fetch("http://localhost:8000/api/auth/user/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
        .then((res) => res.json())
        .then((data) => setUser(data))
        .catch(() => {
          setUser(null);
          setToken(null);
          localStorage.removeItem("token");
        });
    }
  }, [token]);

  const login = (token) => {
    setToken(token);
    localStorage.setItem("token", token);
  };

  const logout = () => {
    fetch("http://localhost:8000/api/auth/logout/", {
      method: "POST",
      headers: {
        Authorization: `Token ${token}`,
      },
    }).finally(() => {
      setUser(null);
      setToken(null);
      localStorage.removeItem("token");
    });
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
