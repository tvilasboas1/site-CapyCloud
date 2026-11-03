from common import ico, WA_MSG, WA, TEL_FMT, TEL_E164, EMAIL


def quemsomos():
    return f"""
<section style="background:#fff">
  <div class="wrap py-16 lg:py-20 grid gap-10 lg:grid-cols-12 items-center">
    <div class="lg:col-span-6 flex justify-center lg:justify-start"><img src="img/capytrio.webp" alt="Quem somos, Capycloud" class="hero-mascot w-full max-w-lg lg:max-w-2xl" width="1400" height="933"></div>
    <div class="lg:col-span-6">
      <h1>Antes de existir como empresa, a gente já resolvia isso todo dia.</h1>
      <p class="lead mt-6">A Capycloud nasceu de profissionais que trabalhavam com virtualização, redes, armazenamento, monitoramento e segurança e viram sempre a mesma cena: empresas pequenas e médias adiando melhorias, convivendo com risco e perdendo dado porque manter TI própria é caro e complicado.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4"><h2>No que acreditamos</h2></div>
    <div class="lg:col-span-8 space-y-6 text-lg">
      <p>A infraestrutura não precisa ser responsabilidade de cada empresa individualmente. Uma equipe especializada pode cuidar do ambiente de várias empresas, reduzindo custo, aumentando segurança e deixando cada cliente focar no próprio negócio. Foi assim que a Capycloud começou, e é assim que ela cresceu para sistemas, suporte, redes e sites: um cliente perguntava "vocês também fazem isso?" e a resposta era sim.</p>
      <p>Nosso objetivo nunca foi vender servidor ou licença. É oferecer uma base sólida, segura e previsível, administrada por quem conhece a operação na prática, para que o cliente concentre esforço em crescer.</p>
      <p>Atendimento faz diferença. Usamos automação para ganhar eficiência, mas quando alguém precisa de ajuda, fala com uma pessoa que conhece o seu ambiente e consegue resolver. Aqui não existe passar por três níveis até achar quem entende da sua rede: quem atende é quem projetou, implantou e administra.</p>
      <p class="quote">Infraestrutura só deveria chamar atenção quando deixa de funcionar. Nossa missão é impedir que isso aconteça.</p>
    </div>
  </div>
</section>

<section class="sec sec-cream">
  <div class="wrap">
    <div class="max-w-3xl mb-10"><h2>O que nos torna diferentes</h2></div>
    <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
      <div><span class="ico-box">{ico('chave')}</span><h3 class="mt-4">Sem dependência de fornecedor</h3><p class="mt-2">Seus dados são seus, sempre. Você não fica preso e pode migrar quando quiser, levando tudo.</p></div>
      <div><span class="ico-box">{ico('alvo')}</span><h3 class="mt-4">Preço em reais</h3><p class="mt-2">Sem surpresa com câmbio. Planos em reais, com previsibilidade de custo.</p></div>
      <div><span class="ico-box">{ico('suporte')}</span><h3 class="mt-4">Suporte em português, por gente</h3><p class="mt-2">Atendimento humano, por especialistas que entendem a sua operação e o seu mercado.</p></div>
      <div><span class="ico-box">{ico('camadas')}</span><h3 class="mt-4">Camadas que se reforçam</h3><p class="mt-2">Monitoramento, automação e segurança trabalham juntos, não como três fornecedores diferentes.</p></div>
    </div>
  </div>
</section>

<section class="sec" style="background:#F8E8D8">
  <div class="wrap grid gap-10 lg:grid-cols-12 items-center">
    <div class="lg:col-span-5 flex justify-center"><img src="img/capySoftwareGrande.webp" alt="Capivara de moletom programando num notebook" class="w-full max-w-sm" width="1400" height="1023" loading="lazy"></div>
    <div class="lg:col-span-7">
      <h2>Software próprio, feito aqui</h2>
      <p class="lead mt-4">A Capycloud desenvolve os próprios sistemas: o MotoGestor, para revendas de motos, e o CapyFiscal, a API de nota fiscal que nasceu dentro dele e hoje é um produto. Tudo roda na nossa infraestrutura, com a nossa equipe cuidando, sem que você precise manter um time de TI.</p>
      <div class="mt-6 flex flex-wrap gap-3"><a class="btn btn-ghost" href="capyfiscal.html">CapyFiscal</a><a class="btn btn-ghost" href="https://motogestor.net.br" target="_blank" rel="noopener noreferrer">MotoGestor</a></div>
    </div>
  </div>
</section>

<section class="sec sec-cream">
  <div class="wrap">
    <div class="max-w-3xl mb-10"><h2>Como funciona na prática</h2><p class="lead mt-4">Do primeiro contato à operação estável, em quatro passos.</p></div>
    <div class="steps" style="grid-template-columns:repeat(auto-fit,minmax(14rem,1fr))">
      <div class="step"><h3>Diagnóstico</h3><p>Conversamos sobre a sua operação, mapeamos o que funciona e o que precisa melhorar. Sem compromisso.</p></div>
      <div class="step"><h3>Projeto</h3><p>Desenhamos a solução para a sua realidade, sem empurrar serviço que você não precisa.</p></div>
      <div class="step"><h3>Implantação</h3><p>Migramos, configuramos e testamos. A sua equipe acompanha cada etapa e valida antes de ir para produção.</p></div>
      <div class="step"><h3>Acompanhamento</h3><p>Monitoramento, manutenção preventiva e atendimento direto com especialistas em horário comercial. Você não fica sozinho.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap"><div class="cta-box">
    <h2>Quer conhecer a Capycloud de perto?</h2>
    <p class="lead mx-auto mt-4">Em uma conversa rápida entendemos a sua operação e mostramos o que dá para fazer.</p>
    <div class="mt-8"><a class="btn btn-gold" href="faleconosco.html">Falar com a equipe</a></div>
  </div></div>
</section>
"""


def faleconosco():
    return f"""
<section class="sec-cream">
  <div class="wrap py-14 lg:py-20">
    <h1>Vamos conversar?</h1>
    <p class="lead mt-5">Conte o que a sua empresa precisa. A gente lê, entende e responde sem enrolação e sem empurrar o plano mais caro.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap grid gap-12 lg:grid-cols-12">
    <div class="lg:col-span-7">
      <h2>Mande uma mensagem</h2>
      <p class="mt-3 muted">O formulário monta a mensagem e abre no seu WhatsApp. Se preferir, use os outros canais ao lado.</p>
      <form id="contact-form" class="mt-8 grid gap-5 sm:grid-cols-2">
        <label class="grid gap-1"><span class="font-semibold text-capy-dark">Seu nome</span><input id="nome" name="nome" required class="rounded-xl border border-capy-borderLight px-4 py-3" autocomplete="name"></label>
        <label class="grid gap-1"><span class="font-semibold text-capy-dark">Empresa</span><input id="empresa" name="empresa" class="rounded-xl border border-capy-borderLight px-4 py-3" autocomplete="organization"></label>
        <label class="grid gap-1 sm:col-span-2"><span class="font-semibold text-capy-dark">Assunto</span>
          <select id="assunto" name="assunto" class="rounded-xl border border-capy-borderLight px-4 py-3 bg-white">
            <option>Cloud privada gerenciada</option><option>CapyFiscal (nota fiscal)</option><option>Suporte técnico ou manutenção remota</option>
            <option>Rede do escritório</option><option>Site novo ou manutenção de site</option><option>Hospedagem ou VPS</option><option>Automação ou integração de sistemas</option><option>Outro assunto</option>
          </select></label>
        <label class="grid gap-1 sm:col-span-2"><span class="font-semibold text-capy-dark">Mensagem</span><textarea id="mensagem" name="mensagem" rows="5" required class="rounded-xl border border-capy-borderLight px-4 py-3" placeholder="Quantas pessoas, quantos computadores, qual sistema usa hoje, o que está doendo."></textarea></label>
        <div class="sm:col-span-2"><button class="btn btn-wa" type="submit">{ico('whatsapp')} Enviar pelo WhatsApp</button></div>
      </form>
    </div>
    <div class="lg:col-span-5 space-y-6">
      <div class="rounded-2xl border border-capy-borderLight p-6">
        <h3>Canais diretos</h3>
        <div class="mt-4 grid gap-3">
          <a class="flex items-center gap-3 link" style="border:0" href="{WA_MSG}" target="_blank" rel="noopener noreferrer">{ico('whatsapp','ico-copper')} WhatsApp: {TEL_FMT}</a>
          <a class="flex items-center gap-3 link" style="border:0" href="https://t.me/+{TEL_E164}" target="_blank" rel="noopener noreferrer">{ico('telegram','ico-copper')} Telegram: mesmo número</a>
          <a class="flex items-center gap-3 link" style="border:0" href="mailto:{EMAIL}">{ico('email','ico-copper')} {EMAIL}</a>
          <a class="flex items-center gap-3 link" style="border:0" href="tel:+{TEL_E164}">{ico('celular','ico-copper')} Ligar: {TEL_FMT}</a>
        </div>
      </div>
      <div class="rounded-2xl bg-capy-cream p-6">
        <h3>Vale saber</h3>
        <ul class="mt-4 space-y-3 text-sm">
          <li class="flex gap-3">{ico('relogio','ico-copper')}<span>Atendimento de segunda a sexta, das 8h às 18h, e aos sábados das 8h às 12h.</span></li>
          <li class="flex gap-3">{ico('suporte','ico-copper')}<span>Cliente com plano abre chamado pela Área do Cliente: a emergência entra na fila certa.</span></li>
          <li class="flex gap-3">{ico('visita','ico-copper')}<span>Visitas técnicas em Brasília e região. Atendimento remoto para o Brasil inteiro.</span></li>
          <li class="flex gap-3">{ico('monitor','ico-copper')}<span>Também atendemos por videochamada para tirar dúvidas sem sair do lugar.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""


def area_do_cliente():
    return f"""
<section class="sec">
  <div class="wrap max-w-2xl text-center py-10">
    <span class="ico-box mx-auto" style="width:4.5rem;height:4.5rem">{ico('painel','ico-lg')}</span>
    <h1 class="mt-6">Área do Cliente</h1>
    <div class="mt-6 rounded-2xl bg-capy-warm p-6 text-left">
      <p class="font-bold text-capy-copper">Em preparação</p>
      <p class="mt-2">A Área do Cliente está sendo preparada. Por ela você vai abrir chamados, acompanhar os seus serviços e entrar no painel do CapyFiscal com um login só.</p>
      <p class="mt-2">Enquanto isso, chamados e dúvidas continuam pelo WhatsApp e pelo e-mail.</p>
    </div>
    <div class="mt-8 flex flex-wrap justify-center gap-3">
      <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener noreferrer">{ico('whatsapp')} Abrir chamado no WhatsApp</a>
      <a class="btn btn-ghost" href="index.html">Voltar ao início</a>
    </div>
  </div>
</section>
"""


def privacidade():
    return f"""
<section class="sec-cream"><div class="wrap py-12 lg:py-16"><h1>Política de privacidade</h1><p class="muted mt-3">Última atualização: outubro de 2026</p></div></section>
<section class="sec"><div class="wrap max-w-3xl space-y-10">
  <div><h2 class="text-2xl">1. Informações que coletamos</h2><p class="mt-3">Coletamos as informações que você fornece diretamente ao preencher formulários de contato, solicitar orçamentos ou contratar nossos serviços: nome, e-mail, telefone, empresa e as informações sobre a sua infraestrutura necessárias à prestação dos serviços.</p><p class="mt-3">Também coletamos dados de uso do site de forma automatizada, como endereço IP, tipo de navegador e páginas visitadas, exclusivamente para melhoria da experiência e segurança.</p></div>
  <div><h2 class="text-2xl">2. Como utilizamos as suas informações</h2><p class="mt-3">Para prestar e gerenciar os serviços contratados; enviar comunicações relacionadas ao serviço; responder a dúvidas e chamados de suporte; melhorar nossos serviços; cumprir obrigações legais e regulatórias.</p></div>
  <div><h2 class="text-2xl">3. Dados fiscais no CapyFiscal</h2><p class="mt-3">Ao usar o CapyFiscal, o seu sistema envia os dados necessários à emissão da nota fiscal, inclusive CPF ou CNPJ, nome e endereço dos destinatários. Esses dados são usados exclusivamente para emitir, consultar e guardar os documentos fiscais pelo prazo legal de 5 anos, e só são acessíveis pela empresa emitente. O certificado digital da empresa é guardado cifrado e usado apenas para assinar os documentos solicitados pelo sistema da própria empresa.</p></div>
  <div><h2 class="text-2xl">4. Compartilhamento de dados</h2><p class="mt-3">A Capycloud não vende, aluga nem compartilha informações pessoais com terceiros para fins comerciais. Os dados podem ser compartilhados apenas com prestadores de serviço que atuam em nosso nome, sob obrigação de confidencialidade, com os órgãos fiscais quando a emissão de documentos assim exigir, e com autoridades competentes quando exigido por lei ou ordem judicial.</p></div>
  <div><h2 class="text-2xl">5. Segurança dos dados</h2><p class="mt-3">Adotamos medidas técnicas e organizacionais para proteger as informações contra acesso não autorizado, destruição, perda ou alteração, com camadas de monitoramento, controle de acesso e backup.</p></div>
  <div><h2 class="text-2xl">6. Seus direitos (LGPD)</h2><p class="mt-3">Você pode confirmar a existência de tratamento, acessar os seus dados, corrigir dados incompletos ou desatualizados, pedir a anonimização ou eliminação de dados desnecessários e revogar o consentimento a qualquer momento. Para isso, escreva para <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p></div>
  <div><h2 class="text-2xl">7. Cookies</h2><p class="mt-3">O site usa apenas cookies essenciais ao funcionamento. Não usamos cookies de rastreamento de terceiros nem para publicidade.</p></div>
  <div><h2 class="text-2xl">8. Contato</h2><p class="mt-3">Dúvidas sobre esta política ou sobre o tratamento dos seus dados: <a class="link" href="mailto:{EMAIL}">{EMAIL}</a> ou <a class="link" href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp {TEL_FMT}</a>.</p></div>
</div></section>
"""
