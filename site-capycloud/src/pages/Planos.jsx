import { Link } from 'react-router-dom';

export default function Planos() {
  const plans = [
    {
      name: 'Básico',
      description: 'Essencial para manter sua operação rodando sem interrupções.',
      price: 'Sob Consulta',
      features: [
        'Suporte Nível 1 (Remoto)',
        'Monitoramento de Rede Básico',
        'Gestão de Backups Diários',
        'Manutenção Preventiva Mensal',
      ],
      highlighted: false,
      buttonText: 'Solicitar Orçamento',
    },
    {
      name: 'Prata',
      description: 'Gestão avançada de infraestrutura e servidores para empresas em crescimento.',
      price: 'Sob Consulta',
      features: [
        'Tudo do plano Básico',
        'Gestão de Virtualização (Proxmox)',
        'Administração de Storage (TrueNAS)',
        'Gestão de Redes e Firewalls (Zentyal/Nginx)',
        'Suporte Nível 2 e SLA Reduzido',
      ],
      highlighted: true, // Este card ganhará destaque visual
      buttonText: 'Falar com Especialista',
    },
    {
      name: 'Ouro',
      description: 'Terceirização completa de TI com foco em governança e alta disponibilidade.',
      price: 'Sob Consulta',
      features: [
        'Tudo do plano Prata',
        'Consultoria em Governança de TI (COSO)',
        'Infraestrutura de Alta Disponibilidade (HA)',
        'Suporte Nível 3 (Presencial/Remoto 24/7)',
        'Planejamento Estratégico de TI',
      ],
      highlighted: false,
      buttonText: 'Agendar Reunião',
    },
  ];

  return (
    <div className="min-h-screen bg-slate-900 py-20 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        
        {/* Cabeçalho da Página */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h1 className="text-4xl font-extrabold text-white tracking-tight sm:text-5xl mb-4">
            Planos de TI <span className="text-emerald-400">Sob Medida</span>
          </h1>
          <p className="text-lg text-slate-400">
            Escolha o nível de gerenciamento ideal para a sua empresa. Da manutenção básica à infraestrutura e governança completas, a Capycloud cuida de tudo.
          </p>
        </div>

        {/* Grid de Planos */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12 items-center">
          {plans.map((plan, index) => (
            <div 
              key={index} 
              className={`relative flex flex-col p-8 rounded-2xl shadow-xl transition-all duration-300 ${
                plan.highlighted 
                  ? 'bg-slate-800 border-2 border-emerald-500 scale-100 md:scale-105 z-10 shadow-emerald-500/20' 
                  : 'bg-slate-800/50 border border-slate-700 hover:border-slate-600 hover:-translate-y-1'
              }`}
            >
              {/* Badge de Destaque para o plano Prata */}
              {plan.highlighted && (
                <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                  <span className="bg-emerald-500 text-slate-950 text-xs font-bold uppercase tracking-wider py-1 px-3 rounded-full">
                    Mais Escolhido
                  </span>
                </div>
              )}

              <div className="mb-8">
                <h3 className={`text-2xl font-bold mb-2 ${plan.highlighted ? 'text-emerald-400' : 'text-white'}`}>
                  {plan.name}
                </h3>
                <p className="text-slate-400 text-sm min-h-[40px]">
                  {plan.description}
                </p>
              </div>

              <div className="mb-8">
                <span className="text-3xl font-extrabold text-white">{plan.price}</span>
              </div>

              <ul className="flex-1 space-y-4 mb-8">
                {plan.features.map((feature, fIndex) => (
                  <li key={fIndex} className="flex items-start">
                    {/* Ícone de Check em SVG (sem precisar de libs extras) */}
                    <svg className={`h-6 w-6 flex-shrink-0 mr-3 ${plan.highlighted ? 'text-emerald-400' : 'text-emerald-500'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span className="text-slate-300 text-sm">{feature}</span>
                  </li>
                ))}
              </ul>

              <Link 
                to="/contato" 
                className={`w-full text-center py-3 px-4 rounded-lg font-bold transition-all ${
                  plan.highlighted
                    ? 'bg-emerald-500 hover:bg-emerald-400 text-slate-950 shadow-lg hover:shadow-emerald-500/30'
                    : 'bg-slate-700 hover:bg-slate-600 text-white'
                }`}
              >
                {plan.buttonText}
              </Link>
            </div>
          ))}
        </div>

        {/* Seção Inferior - FAQ ou Contato Customizado */}
        <div className="mt-20 text-center bg-slate-800/30 border border-slate-700/50 rounded-2xl p-8 sm:p-12">
          <h3 className="text-2xl font-bold text-white mb-4">Precisa de um projeto específico?</h3>
          <p className="text-slate-400 mb-6 max-w-2xl mx-auto">
            Se a sua empresa possui demandas únicas de hardware, migração de datacenters ou requisitos específicos de segurança, podemos desenhar um plano customizado.
          </p>
          <button className="text-emerald-400 font-semibold hover:text-emerald-300 transition-colors inline-flex items-center">
            Montar plano customizado 
            <svg className="ml-2 w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </button>
        </div>

      </div>
    </div>
  );
}