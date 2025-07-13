import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import PlaceDetails from "./pages/PlaceDetails";
import Login from "./pages/Login";
import MainLayout from "./layouts/MainLayout"; // ✅ importa o layout

function App() {
  return (
    <Router>
      <Routes>
        {/* Páginas com layout (Navbar + Footer) */}
        <Route element={<MainLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/places/:id" element={<PlaceDetails />} />
        </Route>

        {/* Página sem layout */}
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
