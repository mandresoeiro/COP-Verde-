# 🌿 COP Verde — Guia Sustentável de Belém

**COP Verde** é uma plataforma interativa desenvolvida para a COP30, com o objetivo de promover o turismo consciente, destacar boas práticas sustentáveis e valorizar a cultura amazônica.

## ✅ Funcionalidades Implementadas

### 1. 🗺️ Mapa Interativo com Filtros
- Exibe locais como hospedagens, feiras, espaços culturais, trilhas e restaurantes.
- Filtros por acessibilidade, impacto ambiental, distância e preço.

### 2. 🧭 Roteiros Personalizados por Perfil
- Usuários informam preferências (veganismo, natureza, arte, turismo histórico).
- Um sistema com IA gera rotas otimizadas com base em localização e tempo disponível.

### 3. ♻️ Avaliação Sustentável
- Cada local pode ser avaliado por critérios como:
  - Apoio à economia local
  - Práticas sustentáveis
  - Uso de materiais recicláveis
  - Conexão com comunidades tradicionais

### 4. 🎭 Experiências Culturais da Amazônia
- Página com eventos paralelos à COP30: oficinas, visitas a comunidades, feiras de saberes.
- Destaques diários com experiências alternativas e locais pouco explorados.

### 5. 🌐 Modo Offline + Multilíngue
- Suporte a funcionamento offline (PWA com Service Workers).
- Traduções para **inglês**, **espanhol** e **francês** com i18n.

### 6. 🤖 Chat com IA Turística
- Assistente inteligente que:
  - Sugere passeios
  - Responde dúvidas sobre a COP30
  - Explica a importância ecológica e cultural de cada local

---

## 🛠️ Stack Tecnológica

| Camada      | Tecnologias                                                  |
|-------------|---------------------------------------------------------------|
| **Backend** | Django + Django Rest Framework + PostgreSQL + GeoDjango       |
| **Frontend**| React (ou Next.js) + Tailwind CSS                             |
| **Mobile**  | PWA ou React Native (futuramente)                             |
| **Mapas**   | Leaflet.js + OpenStreetMap (ou Google Maps API)               |
| **IA**      | OpenAI API ou LangChain                                       |
| **i18n**    | `gettext` (Django) + i18n React                               |
| **Offline** | PWA com Service Workers                                       |

---

## 🚀 Como rodar localmente

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

# Frontend
cd frontend
npm install
npm run dev
