import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header.jsx';

// Importando as páginas que você acabou de criar
import Home from './pages/Home.jsx';
import Servicos from './pages/Servicos.jsx';
import Vantagens from './pages/Vantagens.jsx';
import Planos from './pages/Planos.jsx';

export default function App() {
  return (
    <BrowserRouter>
      <div className="bg-slate-900 font-sans text-white min-h-screen">
        {/* O Header fica fora das rotas, assim ele aparece em todas as páginas! */}
        <Header />

        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/servicos" element={<Servicos />} />
            <Route path="/vantagens" element={<Vantagens />} />
            <Route path="/planos" element={<Planos />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}