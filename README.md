# 🌿 COP Verde — Guia Sustentável de Belém

**COP Verde** é uma plataforma interativa em desenvolvimento para apoiar a COP30 em Belém, promovendo turismo consciente, práticas sustentáveis e valorização da cultura amazônica.

---

## 🚧 Funcionalidades em Desenvolvimento

### 1. 🗺️ Mapa Interativo com Filtros
- [ ] Exibição de hospedagens, restaurantes, feiras, espaços culturais, trilhas ecológicas e transportes limpos.
- [ ] Filtros por acessibilidade, impacto ambiental, distância e preço.

### 2. 🧭 Roteiros Personalizados por Perfil
- [ ] Usuário informa preferências (veganismo, arte, natureza, turismo histórico).
- [ ] Sistema de IA gera rotas otimizadas com base em localização, tempo e agenda.

### 3. ♻️ Avaliação Sustentável
- [ ] Locais avaliados por impacto ambiental, apoio à economia local e boas práticas.
- [ ] Visitantes podem deixar notas como: "carbono neutro", "usa recicláveis", "apoia ribeirinhos".

### 4. 🎭 Experiências Culturais da Amazônia
- [ ] Agenda de eventos paralelos à COP30 (rodas de conversa, oficinas, arte urbana, feiras).
- [ ] Destaques diários e sugestões de turismo alternativo.

### 5. 🌐 Modo Offline + Multilíngue
- [ ] Plataforma acessível offline (roteiros salvos).
- [ ] Tradução para inglês, espanhol e francês.

### 6. 🤖 Chat com IA Turística
- [ ] Assistente inteligente com sugestões, explicações dos locais e suporte ao visitante.

---

## 🛠️ Stack Tecnológica (proposta)

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
