from common import ico, WA_MSG

NODES_HERO = """
<div class="nodes" aria-hidden="true">
  <svg viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice">
    <line x1="80" y1="120" x2="260" y2="60"/><line x1="260" y1="60" x2="420" y2="150"/><line x1="80" y1="120" x2="140" y2="330"/>
    <line x1="140" y1="330" x2="420" y2="150"/><line x1="140" y1="330" x2="90" y2="560"/><line x1="420" y1="150" x2="520" y2="40"/>
    <line x1="1120" y1="90" x2="980" y2="200"/><line x1="980" y1="200" x2="1150" y2="330"/><line x1="1150" y1="330" x2="1040" y2="520"/>
    <line x1="980" y1="200" x2="1040" y2="520"/><line x1="1040" y1="520" x2="900" y2="640"/>
    <circle cx="80" cy="120" r="4"/><circle cx="260" cy="60" r="5"/><circle cx="420" cy="150" r="4"/><circle cx="140" cy="330" r="5"/>
    <circle cx="90" cy="560" r="3.5"/><circle cx="520" cy="40" r="3.5"/><circle cx="1120" cy="90" r="4"/><circle cx="980" cy="200" r="5"/>
    <circle cx="1150" cy="330" r="4"/><circle cx="1040" cy="520" r="5"/><circle cx="900" cy="640" r="3.5"/>
    <circle class="big" cx="260" cy="60" r="11"/><circle class="big" cx="1040" cy="520" r="11"/>
  </svg>
</div>"""


def frentes(coluna=False):
    return f"""
<div class="fronts{' fronts-col' if coluna else ''}">
  <a class="front" href="servicos.html#infraestrutura">{ico('host','ico-lg ico-copper')}<div><strong>Cloud privada gerenciada</strong><small>Arquivos, acessos, backup e segurança num ambiente só seu, cuidado pela gente.</small></div></a>
  <a class="front" href="servicos.html#sistemas">{ico('automacao','ico-lg ico-copper')}<div><strong>Sistemas e automação</strong><small>CapyFiscal, MotoGestor, rotinas automáticas e integrações entre os sistemas que você já usa.</small></div></a>
  <a class="front" href="servicos.html#suporte">{ico('suporte','ico-lg ico-copper')}<div><strong>Suporte técnico</strong><small>Chamado aberto, alguém que conhece o seu ambiente responde. Remoto ou na sua empresa.</small></div></a>
  <a class="front" href="servicos.html#redes">{ico('cabo','ico-lg ico-copper')}<div><strong>Redes e cabeamento</strong><small>Projeto, passagem de cabos, rack, Wi-Fi e firewall. Rede que funciona e fica organizada.</small></div></a>
  <a class="front" href="servicos.html#sites">{ico('site','ico-lg ico-copper')}<div><strong>Sites e hospedagem</strong><small>Criação, manutenção do site que você já tem e hospedagem gerenciada de sistemas.</small></div></a>
</div>"""


def home():
    return f"""
<section class="relative overflow-hidden" style="background:#fff">
  {NODES_HERO}
  <div class="wrap relative grid gap-10 lg:grid-cols-12 items-center py-16 lg:py-24">
    <div class="lg:col-span-6 flex justify-center lg:justify-start">
      <img src="img/capy66.webp" alt="Capycloud, infraestrutura digital e soluções" class="hero-mascot mascot-shadow w-full max-w-lg lg:max-w-2xl" width="1400" height="764">
    </div>
    <div class="lg:col-span-6">
      <h1>A TI da sua empresa, resolvida por gente que atende.</h1>
      <p class="lead mt-6">Infraestrutura, sistemas, suporte, redes e sites. Você explica o problema uma vez, e quem projeta, implanta e mantém é a mesma equipe. Mensalidade fixa onde dá para ser fixa; orçamento claro onde cada caso é um caso.</p>
      <div class="mt-8 flex flex-wrap gap-3">
        <a class="btn btn-gold" href="faleconosco.html">Pedir um diagnóstico</a>
        <a class="btn btn-ghost" href="servicos.html">Ver todos os serviços</a>
      </div>
      <p class="mt-6 text-sm muted">Atendimento de segunda a sexta, das 8h às 18h, e aos sábados até o meio-dia. Brasília e região, com atendimento remoto para o Brasil inteiro.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="max-w-3xl mb-10">
      <h2>Cinco frentes, uma equipe</h2>
      <p class="lead mt-4">A maioria dos nossos clientes começa por uma e vai chamando as outras conforme a empresa cresce.</p>
    </div>
    <div class="grid gap-10 lg:grid-cols-12 items-center">
      <div class="lg:col-span-7 flex justify-center">
        <img src="img/capyservindex.webp" alt="Ecossistema Capycloud, diagrama das soluções integradas" class="w-full h-auto" width="1400" height="933" loading="lazy">
      </div>
      <div class="lg:col-span-5">
        {frentes(coluna=True)}
        <a class="link mt-6 inline-block" href="planos.html">Ver planos e preços</a>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-dark relative overflow-hidden">
  <div class="wrap grid gap-10 lg:grid-cols-12 items-center">
    <div class="lg:col-span-7">
      <p class="kicker" style="color:#E7C77A">Novo</p>
      <h2>CapyFiscal: a nota fiscal sai do seu sistema, sem você virar contador</h2>
      <p class="lead mt-5" style="color:#D9CDBD">Uma API de emissão de NF-e compatível com os padrões de mercado. O seu sistema manda os dados da venda, o CapyFiscal assina com o certificado da empresa, conversa com a SEFAZ e devolve o XML e o DANFE. Com guarda dos arquivos por cinco anos e aviso automático quando a nota muda de situação.</p>
      <div class="mt-8 flex flex-wrap gap-3">
        <a class="btn btn-gold" href="capyfiscal.html">Conhecer o CapyFiscal</a>
        <a class="btn btn-ghost" style="color:#E8DFD2;border-color:#6B625A" href="capyfiscal.html#planos">Planos a partir de R$ 89/mês</a>
      </div>
    </div>
    <div class="lg:col-span-5">
      <div class="rounded-2xl p-6" style="background:#3A3531;border:1px solid #4E4742">
        <p class="font-bold text-white">O que vem no pacote</p>
        <ul class="mt-4 space-y-3" style="color:#D9CDBD">
          <li class="flex gap-3">{ico('nfe','ico-copper')}<span>NF-e modelo 55, com cancelamento, carta de correção e inutilização</span></li>
          <li class="flex gap-3">{ico('webhook','ico-copper')}<span>Aviso automático (webhook) quando a nota é autorizada, rejeitada ou cancelada</span></li>
          <li class="flex gap-3">{ico('pdf','ico-copper')}<span>XML e DANFE guardados por 5 anos, prontos para o contador</span></li>
          <li class="flex gap-3">{ico('painel','ico-copper')}<span>Painel dentro da Área do Cliente, com um login só</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-cream">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-5">
      <h2>Por que empresas pequenas e médias escolhem a Capycloud</h2>
      <p class="lead mt-4">Não é pela tecnologia. É por não precisar pensar nela.</p>
    </div>
    <div class="lg:col-span-7 grid gap-6 sm:grid-cols-2">
      <div><h3>Você sabe quanto paga</h3><p class="mt-2">Cloud, CapyFiscal, hospedagem e manutenção têm mensalidade fixa. O que depende do caso (suporte, cabeamento, site) vem com orçamento antes de qualquer serviço.</p></div>
      <div><h3>Quem atende conhece o seu ambiente</h3><p class="mt-2">Sem fila de níveis de atendimento. Você fala com quem configurou a sua rede, o seu servidor ou o seu sistema.</p></div>
      <div><h3>Seus dados continuam seus</h3><p class="mt-2">Ambiente dedicado, backup diário com cópia fora do escritório e nenhuma amarra: quando quiser, leva tudo embora.</p></div>
      <div><h3>Cresce no seu ritmo</h3><p class="mt-2">Contratou mais gente, abriu filial, precisou emitir nota? A estrutura acompanha sem comprar servidor novo nem contratar um técnico.</p></div>
      <div><h3>Software livre por baixo</h3><p class="mt-2">A infraestrutura roda sobre tecnologias abertas, sem licença por usuário e sem preço em dólar.</p></div>
      <div><h3>Gente, não robô</h3><p class="mt-2">Usamos automação para não deixar nada passar, mas quem responde o seu chamado é uma pessoa, em português, em horário comercial.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-box">
      <h2>Quer ver se faz sentido para a sua empresa?</h2>
      <p class="lead mx-auto mt-4">Em uma conversa de meia hora a gente entende como você trabalha hoje e diz, sem compromisso, o que dá para melhorar e quanto custa.</p>
      <div class="mt-8 flex flex-wrap justify-center gap-3">
        <a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener noreferrer">{ico('whatsapp')} Conversar no WhatsApp</a>
        <a class="btn btn-dark" href="faleconosco.html">Outras formas de contato</a>
      </div>
    </div>
  </div>
</section>
"""


def _row(icone, titulo, texto, tag):
    rot = {"mes": ("tag tag-mes", "Mensalidade"), "analise": ("tag tag-analise", "Orçamento após análise"),
           "projeto": ("tag tag-projeto", "Por projeto")}[tag]
    return f"""
    <div class="ledger-row">
      <span class="ico-box">{ico(icone)}</span>
      <div><h3>{titulo}</h3><p>{texto}</p></div>
      <span class="{rot[0]}">{rot[1]}</span>
    </div>"""


def servicos():
    return f"""
<section class="relative overflow-hidden" style="background:#fff">
  {NODES_HERO}
  <div class="wrap relative py-16 lg:py-20 grid gap-8 lg:grid-cols-12 items-center">
    <div class="lg:col-span-5 flex justify-center lg:justify-start"><img src="img/capysorri.webp" alt="Serviços Capycloud" class="hero-mascot w-full max-w-sm lg:max-w-md" width="1400" height="1400"></div>
    <div class="lg:col-span-7">
      <h1>O que a Capycloud faz pela sua empresa</h1>
      <p class="lead mt-5">Cinco frentes de trabalho. Em cada serviço dizemos como cobramos: mensalidade fixa, orçamento depois de olhar o seu caso, ou por projeto fechado. Sem preço de tabela para o que depende da sua realidade.</p>
      <div class="mt-6 flex flex-wrap gap-2">
        <a class="tag" href="#infraestrutura">Cloud privada</a><a class="tag" href="#sistemas">Sistemas e automação</a><a class="tag" href="#suporte">Suporte e manutenção</a><a class="tag" href="#redes">Rede do escritório</a><a class="tag" href="#sites">Sites e hospedagem</a>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="infraestrutura">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4 lg:sticky lg:top-28 self-start">
      <h2>Cloud privada gerenciada</h2>
      <p class="mt-4">Os seus arquivos, acessos, backup e segurança num ambiente dedicado, administrado pela gente. É o que vendemos em planos, de R$ 999 a R$ 3.599 por mês.</p>
      <a class="link inline-block mt-4" href="planos.html#cloud">Ver os planos de cloud</a>
    </div>
    <div class="lg:col-span-8 ledger">
      {_row('arquivos','Servidor de arquivos centralizado','Os documentos da empresa num só lugar, acessíveis de qualquer computador, com versões anteriores e sem o "tá na minha máquina". Por dentro é o CapyDrive.','mes')}
      {_row('vpn','Acesso remoto por VPN','A equipe entra no sistema da empresa de casa ou da rua com a mesma segurança de estar no escritório. CapyNet.','mes')}
      {_row('usuarios','Usuários e permissões','Cada pessoa acessa só o que precisa. Entrou, cria o acesso; saiu, bloqueia em segundos. Conformidade com a LGPD. CapyAD.','mes')}
      {_row('backup','Backup automatizado','Todo dia, sozinho, com cópia fora do escritório e versões anteriores. Se algo der errado, a gente recupera. CapyBackup.','mes')}
      {_row('monitor','Monitoramento contínuo','Acompanhamos a saúde do ambiente em horário comercial e agimos antes de o problema chegar em você. CapyMonitor.','mes')}
      {_row('firewall','Firewall e segurança de perímetro','Uma barreira entre a sua rede e a internet. Tráfego suspeito bloqueado, infraestrutura invisível para quem não deveria chegar perto.','mes')}
      {_row('seguranca','Segurança da informação','Detecção de intrusão, análise de vulnerabilidades e resposta a incidentes para quem lida com dados sensíveis. CapySec.','mes')}
      {_row('auditoria','Auditoria e relatórios','Quem acessou o quê e quando, com histórico e relatórios prontos para a LGPD.','mes')}
    </div>
  </div>
</section>

<section class="sec sec-cream" id="sistemas">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4 lg:sticky lg:top-28 self-start">
      <h2>Sistemas e automação</h2>
      <p class="mt-4">Software próprio e automações feitas para o jeito que a sua empresa trabalha. É o que o mercado mais pede, e é onde a Capycloud mais cresce.</p>
      <a class="link inline-block mt-4" href="capyfiscal.html">Conhecer o CapyFiscal</a>
    </div>
    <div class="lg:col-span-8 ledger">
      {_row('nfe','CapyFiscal, emissão de NF-e por API','O seu sistema manda os dados, o CapyFiscal assina, envia para a SEFAZ e devolve XML e DANFE. Compatível com os padrões de mercado, guarda por 5 anos, painel na Área do Cliente.','mes')}
      {_row('automacao','MotoGestor, gestão para lojas de motos','Estoque, vendas, contratos e notas promissórias para revendas de motos usadas, com integração ao RENAVE e NF-e pelo CapyFiscal. Oficinas em desenvolvimento.','mes')}
      {_row('camadas','Automações de rotina','Cobranças, lembretes, relatórios diários no WhatsApp, planilhas que se preenchem sozinhas. Rotinas que hoje alguém faz na mão viram fluxos automáticos.','analise')}
      {_row('rede','Integrações entre sistemas','O sistema de vendas conversa com o financeiro, o site conversa com o estoque, a planilha conversa com o ERP. Sem redigitar nada.','analise')}
      {_row('alvo','Sistema sob medida','Quando nada pronto resolve, a gente desenvolve. Começa pequeno, entra em uso cedo e cresce com o que o uso real mostrar.','projeto')}
    </div>
  </div>
</section>

<section class="sec" id="suporte">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4 lg:sticky lg:top-28 self-start">
      <h2>Suporte técnico e manutenção</h2>
      <p class="mt-4">Para quem não tem TI interna e cansou de chamar "o sobrinho". Chamado aberto, alguém que conhece o seu ambiente responde.</p>
      <a class="link inline-block mt-4" href="planos.html#manutencao">Ver a manutenção remota mensal</a>
    </div>
    <div class="lg:col-span-8 ledger">
      {_row('remoto','Manutenção remota mensal','Uma mensalidade e a Capycloud vira a TI da sua empresa: computadores, rede, e-mail, impressora de rede, sistemas. Atendimento remoto em horário comercial, com horas incluídas e visita quando precisar. Valor fechado depois de conhecer o seu ambiente.','analise')}
      {_row('suporte','Chamados avulsos','Precisou de uma vez só? Abra o chamado, a gente avalia, passa o valor e resolve. Remoto ou presencial em Brasília e região.','analise')}
      {_row('visita','Visita técnica','Instalação de equipamento, configuração de máquinas novas, diagnóstico no local. Valor por visita, combinado antes.','analise')}
      {_row('manutencao','Manutenção preventiva','Atualizações, limpeza, ajustes e correções feitos com antecedência, antes de virarem incêndio. Entra na mensalidade ou por visita.','analise')}
      {_row('relogio','Emergências','Servidor fora, sistema parado, banco de dados com erro: prioridade na fila, inclusive fora do horário para clientes com plano.','mes')}
    </div>
  </div>
</section>

<section class="sec sec-cream" id="redes">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4 lg:sticky lg:top-28 self-start">
      <h2>Rede do escritório</h2>
      <p class="mt-4">Para escritórios, lojas e consultórios. Internet que cai, Wi-Fi que não chega na sala dos fundos, cabo solto atrás do balcão: a gente organiza e deixa funcionando.</p>
    </div>
    <div class="lg:col-span-8 ledger">
      {_row('cabo','Pontos de rede','Pontos novos, troca de cabos e identificação de cada ponto, em ambientes de pequeno porte.','projeto')}
      {_row('host','Organização do rack','Switch, roteador e cabos arrumados e etiquetados. Quando der problema, todo mundo sabe onde mexer.','projeto')}
      {_row('mapa','Wi-Fi','Sinal em todos os cômodos, rede separada para clientes e para a equipe.','projeto')}
      {_row('firewall','Firewall','Bloqueio do que não deve entrar e acesso seguro para quem trabalha de fora.','analise')}
      {_row('manutencao','Manutenção','Diagnóstico e troca de equipamento. Sem contrato fixo quando é uma vez só.','analise')}
    </div>
  </div>
</section>

<section class="sec" id="sites">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4 lg:sticky lg:top-28 self-start">
      <h2>Sites e hospedagem</h2>
      <p class="mt-4">Site novo, site que já existe e precisa de quem cuide, ou um lugar seguro para rodar o sistema que você já usa.</p>
      <a class="link inline-block mt-4" href="planos.html#hospedagem">Ver hospedagem e VPS</a>
    </div>
    <div class="lg:col-span-8 ledger">
      {_row('site','Criação de sites','Site institucional ou página de captação, rápido, no seu domínio, pronto para o Google. Conteúdo escrito junto com você.','projeto')}
      {_row('manutencao','Manutenção de site existente','O site já existe, mas ninguém atualiza, o certificado venceu, a página caiu? Mensalidade com atualizações, backup, monitoramento e pequenas alterações incluídas.','mes')}
      {_row('vps','Hospedagem gerenciada e VPS','Servidor virtual para o seu sistema, loja virtual ou aplicação de terceiros, com instalação, atualizações, backup e monitoramento por nossa conta. CapyHost.','mes')}
      {_row('pasta5','Armazenamento em nuvem','Espaço extra para backup ou para compartilhar arquivos grandes, com criptografia, sem precisar do pacote completo.','mes')}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap grid gap-8 lg:grid-cols-12 items-center">
    <div class="lg:col-span-7">
      <h2>Não achou o que precisa na lista?</h2>
      <p class="lead mt-4">Descreva o problema. Se não for com a gente, indicamos quem resolve.</p>
    </div>
    <div class="lg:col-span-5 flex flex-wrap gap-3 lg:justify-end">
      <a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener noreferrer">{ico('whatsapp')} Perguntar no WhatsApp</a>
      <a class="btn btn-dark" href="faleconosco.html">Falar com a equipe</a>
    </div>
  </div>
</section>
"""
