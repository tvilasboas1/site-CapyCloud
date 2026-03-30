export default function Header() {
  return (
    <header className="bg-slate-900/90 backdrop-blur-md sticky top-0 z-50 border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          
          {/* Logo da Capycloud */}
          <div className="flex-shrink-0 flex items-center cursor-pointer">
            <span className="text-3xl font-extrabold text-emerald-400 tracking-tighter">Capy</span>
            <span className="text-3xl font-bold text-white tracking-tighter">cloud</span>
          </div>

          {/* Links de Navegação (Escondidos no celular, visíveis no PC) */}
          <nav className="hidden md:flex space-x-8">
            <a href="#servicos" className="text-slate-300 hover:text-emerald-400 transition-colors font-medium">Serviços</a>
            <a href="#vantagens" className="text-slate-300 hover:text-emerald-400 transition-colors font-medium">Vantagens</a>
            <a href="#planos" className="text-slate-300 hover:text-emerald-400 transition-colors font-medium">Planos</a>
          </nav>

          {/* Botão de Ação (CTA) */}
          <div className="hidden md:flex items-center">
            <button className="bg-emerald-500 hover:bg-emerald-400 text-slate-900 px-6 py-2.5 rounded-lg font-bold transition-all shadow-lg hover:shadow-emerald-500/30 hover:-translate-y-0.5">
              Falar com Especialista
            </button>
          </div>

          {/* Botão de Menu para Celular (Ícone Hamburguer) */}
          <div className="md:hidden flex items-center">
            <button className="text-slate-300 hover:text-white focus:outline-none">
              <svg className="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>

        </div>
      </div>
    </header>
  );
}