import { Link } from 'react-router-dom';

// Um pequeno componente helper para os cards de serviço
const ServiceCard = ({ icon, title, description }) => (
  <div className="bg-slate-800 p-8 rounded-2xl border border-slate-700 shadow-xl hover:border-emerald-700 transition duration-300 group">
    <div className="text-4xl text-emerald-400 mb-5 group-hover:scale-110 transition-transform duration-300">
      {icon}
    </div>
    <h3 className="text-2xl font-bold text-white mb-3 tracking-tight">{title}</h3>
    <p className="text-slate-300 leading-relaxed text-base">{description}</p>
  </div>
);

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-900 text-white font-sans">
      
      {/* --- SEÇÃO HERO (Topo de Impacto) --- */}
      <section className="relative pt-32 pb-24 px-4 bg-gradient-to-br from-slate-950 via-slate-900 to-emerald-950/20 overflow-hidden">
        {/* Um detalhe visual abstrato de fundo */}
        <div className="absolute inset-0 opacity-10">
          <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <pattern id="dotPattern" patternUnits="userSpaceOnUse" width="32" height="32">
                <circle cx="1" cy="1" r="1" fill="#10b981" />
              </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#dotPattern)" />
          </svg>
        </div>

        <div className="max-w-5xl mx-auto text-center relative z-10">
          <h1 className="text-6xl md:text-7xl font-extrabold tracking-tighter leading-tight">
            Tire o peso da TI das <br className="hidden md:block"/>
            suas costas com a <span className="text-emerald-400">Capycloud</span>.
          </h1>
          <p className="mt-8 text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Monitoramento proativo, segurança de ponta e suporte especializado 24/7. Deixe-nos cuidar da sua infraestrutura enquanto você foca no crescimento do seu negócio.
          </p>
          <div className="mt-12 flex flex-col sm:flex-row gap-5 justify-center">
            <Link 
              to="/planos" 
              className="bg-emerald-500 hover:bg-emerald-400 text-slate-950 px-10 py-4 rounded-xl font-bold text-lg transition-all shadow-lg hover:shadow-emerald-500/30 hover:-translate-y-0.5"
            >
              Conhecer Nossos Planos
            </Link>
            <button className="bg-slate-800 hover:bg-slate-700 text-white px-10 py-4 rounded-xl font-medium text-lg transition-all border border-slate-700">
              Solicitar Orçamento Grátis
            </button>
          </div>
        </div>
      </section>

      {/* --- SEÇÃO SERVIÇOS (Grid Profissional) --- */}
      <section className="py-24 px-4 bg-slate-950">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16 max-w-2xl mx-auto">
            <h2 className="text-sm font-semibold text-emerald-400 uppercase tracking-widest mb-3">Nossas Soluções</h2>
            <p className="text-4xl font-bold tracking-tight text-white sm:text-5xl">
              Focados na estabilidade da <span className="text-emerald-400">sua empresa</span>.
            </p>
          </div>

          {/* O Grid de serviços (Grosso antes de modelar) */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <ServiceCard 
              icon="🛠️"
              title="Monitoramento NOC 24/7"
              description="Nossa equipe vigia sua rede em tempo real para corrigir falhas antes mesmo que você perceba que elas existiram."
            />
            <ServiceCard 
              icon="☁️"
              title="Gerenciamento Cloud"
              description="Otimizamos custos e performance na AWS, Azure ou Google Cloud com migração segura e arquitetura escalável."
            />
            <ServiceCard 
              icon="🛡️"
              title="Segurança e Backup"
              description="Implementação de SOC, firewalls avançados e rotinas automatizadas de backup em nuvem contra ransomware."
            />
          </div>
        </div>
      </section>

    </div>
  );
}