import { Link } from 'react-router-dom';

export default function Vantagens() {
  const advantages = [
    {
      title: 'Segurança Proativa e Blue Team',
      description: 'Não esperamos o ataque acontecer. Implementamos monitoramento contínuo, gestão de vulnerabilidades e defesa ativa para proteger seus ativos mais críticos antes que as ameaças atinjam sua rede.',
      icon: (
        <svg className="w-8 h-8 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
        </svg>
      )
    },
    {
      title: 'Alta Disponibilidade com Virtualização',
      description: 'Chega de servidores físicos ociosos ou pontos únicos de falha. Desenhamos ambientes virtuais otimizados e redundantes, garantindo que suas aplicações vitais continuem rodando mesmo se um hardware falhar.',
      icon: (
        <svg className="w-8 h-8 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
        </svg>
      )
    },
    {
      title: 'Proteção de Dados e Storage Blindado',
      description: 'Sua informação é o coração do negócio. Configuramos rotinas de backup automatizadas, retenção segura e storage inteligente, garantindo recuperação rápida contra falhas físicas ou ataques de ransomware.',
      icon: (
        <svg className="w-8 h-8 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
        </svg>
      )
    },
    {
      title: 'Automação de Processos',
      description: 'Substituímos o trabalho manual por scripts e automações inteligentes. Reduzimos o erro humano e aumentamos a eficiência operacional da sua equipe, deixando a tecnologia trabalhar por você.',
      icon: (
        <svg className="w-8 h-8 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
      )
    }
  ];

  return (
    <div className="min-h-screen bg-slate-900 py-20 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        
        {/* Cabeçalho */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h1 className="text-4xl font-extrabold text-white tracking-tight sm:text-5xl mb-4">
            Por que escolher a <span className="text-emerald-400">Capycloud?</span>
          </h1>
          <p className="text-lg text-slate-400">
            Nossa abordagem vai além do suporte técnico tradicional. Entregamos uma infraestrutura de ponta a ponta projetada para resiliência e performance.
          </p>
        </div>

        {/* Grid de Vantagens (Layout Alternado) */}
        <div className="space-y-16">
          {advantages.map((adv, index) => (
            <div 
              key={index} 
              className={`flex flex-col md:flex-row items-center gap-8 md:gap-12 ${
                index % 2 !== 0 ? 'md:flex-row-reverse' : ''
              }`}
            >
              {/* Bloco de Texto */}
              <div className="flex-1 space-y-4">
                <div className="inline-flex items-center justify-center p-3 bg-slate-800 rounded-xl border border-slate-700 shadow-sm mb-2">
                  {adv.icon}
                </div>
                <h3 className="text-2xl font-bold text-white">{adv.title}</h3>
                <p className="text-slate-400 leading-relaxed text-lg">
                  {adv.description}
                </p>
              </div>

              {/* Bloco Visual Decorativo (Representa o sistema) */}
              <div className="flex-1 w-full">
                <div className="relative rounded-2xl bg-gradient-to-br from-slate-800 to-slate-900 border border-slate-700 p-6 md:p-8 overflow-hidden group">
                  {/* Padrão de Fundo (Grid) */}
                  <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                  
                  {/* Elemento Gráfico Fake para dar cara de "Dashboard" */}
                  <div className="relative z-10 flex flex-col gap-4">
                    <div className="h-4 bg-slate-700/50 rounded w-1/3 group-hover:bg-emerald-500/20 transition-colors"></div>
                    <div className="h-4 bg-slate-700/50 rounded w-full group-hover:bg-emerald-500/20 transition-colors delay-75"></div>
                    <div className="h-4 bg-slate-700/50 rounded w-5/6 group-hover:bg-emerald-500/20 transition-colors delay-150"></div>
                    <div className="mt-4 flex gap-2">
                      <div className="h-8 w-8 rounded-full bg-emerald-500/20 flex items-center justify-center">
                        <div className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></div>
                      </div>
                      <div className="h-8 flex-1 bg-slate-700/30 rounded"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Call to Action Final */}
        <div className="mt-24 text-center">
          <div className="bg-emerald-500/10 border border-emerald-500/20 rounded-2xl p-10 max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-white mb-4">Pronto para elevar o nível da sua TI?</h2>
            <p className="text-slate-300 mb-8 max-w-2xl mx-auto">
              Pare de gastar tempo resolvendo problemas de rotina. Deixe a Capycloud blindar sua operação enquanto você foca no seu negócio.
            </p>
            <Link 
              to="/planos" 
              className="inline-block bg-emerald-500 hover:bg-emerald-400 text-slate-950 px-8 py-3.5 rounded-lg font-bold transition-all shadow-lg hover:shadow-emerald-500/30 hover:-translate-y-0.5"
            >
              Ver Planos Disponíveis
            </Link>
          </div>
        </div>

      </div>
    </div>
  );
}