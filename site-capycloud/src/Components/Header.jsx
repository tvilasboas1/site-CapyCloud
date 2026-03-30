import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className="bg-slate-900/90 backdrop-blur-md sticky top-0 z-50 border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          
          {/* Logo da Capycloud agora é um Link para a Home ("/") */}
          <Link to="/" className="flex-shrink-0 flex items-center cursor-pointer">
            <span className="text-3xl font-extrabold text-emerald-400 tracking-tighter">Capy</span>
            <span className="text-3xl font-bold text-white tracking-tighter">cloud</span>
          </Link>

          {/* Links de Navegação usando o router */}
          <nav className="hidden md:flex space-x-8">
            <Link to="/servicos" className="text-slate-300 hover:text-emerald-400 transition-colors font-medium">Serviços</Link>
            <Link to="/vantagens" className="text-slate-300 hover:text-emerald-400 transition-colors font-medium">Vantagens</Link>
            <Link to="/planos" className="text-slate-300 hover:text-emerald-400 transition-colors font-medium">Planos</Link>
          </nav>

          <div className="hidden md:flex items-center">
            <button className="bg-emerald-500 hover:bg-emerald-400 text-slate-900 px-6 py-2.5 rounded-lg font-bold transition-all shadow-lg hover:shadow-emerald-500/30 hover:-translate-y-0.5">
              Falar com Especialista
            </button>
          </div>

        </div>
      </div>
    </header>
  );
}
