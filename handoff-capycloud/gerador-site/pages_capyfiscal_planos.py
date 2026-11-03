from common import ico, WA_MSG


def hero_orig(titulo_html, texto, alt, ancora="", img="img/capidev_fundobranco.webp", tam=(1400, 933)):
    """Topo no mesmo molde das páginas originais (Serviços, Quem Somos): fundo branco, capivara à esquerda, texto à direita.
    A imagem é provisória (capidev_fundobranco); quando chegar a arte própria, troque só o src."""
    id_html = f' id="{ancora}"' if ancora else ""
    return f"""
  <section{id_html} class="py-20 px-4 sm:px-6 lg:px-8 bg-white">
    <div class="max-w-7xl mx-auto">
      <div class="flex flex-col lg:flex-row items-center gap-10 lg:gap-16">

        <!-- LADO ESQUERDO: Mascote -->
        <div class="w-full lg:w-1/2 flex justify-center reveal opacity-0 delay-100">
          <img src="{img}" alt="{alt}" class="w-full max-w-2xl sm:max-w-3xl lg:max-w-5xl fx-float" width="{tam[0]}" height="{tam[1]}">
        </div>

        <!-- LADO DIREITO: Título -->
        <div class="w-full lg:w-1/2 text-center lg:text-left">
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-capy-dark mb-6 tracking-normal leading-tight">
            {titulo_html}
          </h1>
          <p class="text-capy-text text-lg leading-relaxed mb-6 text-justify">
            {texto}
          </p>
        </div>

      </div>
    </div>
  </section>
"""

# ------------------------------------------------------------------ planos do CapyFiscal (um só lugar, usado em duas páginas)
def planos_capyfiscal(com_titulo=True):
    def plan(nome, quem, preco, nota, itens, hi=False, cta="Quero este plano"):
        lis = "".join(f"<li>{ico('check')}<span>{i}</span></li>" for i in itens)
        return f"""
      <div class="plan{' plan-hi' if hi else ''}">
        <h3>{nome}</h3><p class="who">{quem}</p>
        <div class="price"><strong>R$ {preco}</strong><span>/mês</span></div>
        <p class="price-note">{nota}</p>
        <ul>{lis}</ul>
        <a class="btn btn-gold" href="faleconosco.html">{cta}</a>
      </div>"""
    titulo = """
    <div class="mb-10">
      <h2>Planos do CapyFiscal</h2>
      <p class="lead mt-4">Preço mensal, sem taxa de adesão e sem fidelidade. As notas que passarem da franquia são cobradas por unidade no mês seguinte. Todos os planos incluem ambiente de testes sem limite, XML e DANFE guardados por 5 anos, avisos por webhook e painel na Área do Cliente.</p>
    </div>""" if com_titulo else ""
    return f"""
    {titulo}
    <div class="plans plans-3">
      {plan('Loja', '1 CNPJ', '89', 'Até 100 NF-e por mês<br>Nota adicional: R$ 0,15',
            ['Emissão, cancelamento, carta de correção e inutilização', 'Nota de saída e de entrada, inclusive compra de pessoa física',
             'DANFE em PDF e XML autorizado', 'Aviso por webhook a cada mudança de situação', 'Suporte por WhatsApp em horário comercial'])}
      {plan('Rede', 'Até 3 CNPJs', '149', 'Até 300 NF-e por mês<br>Nota adicional: R$ 0,12',
            ['Tudo do plano Loja', 'Matriz e filiais no mesmo painel', 'Pacote mensal de XMLs enviado ao seu contador',
             'Relatório mensal de notas por empresa', 'Aviso de vencimento do certificado digital'], hi=True)}
      {plan('Integrador', 'CNPJs ilimitados', '349', 'Até 1.500 NF-e por mês<br>Nota adicional: R$ 0,10',
            ['Tudo do plano Rede', 'Feito para software houses e ERPs que emitem para os próprios clientes',
             'Cadastro de empresas pela API', 'Suporte técnico direto com quem desenvolve a API', 'Acompanhamento na homologação do seu sistema'],
            cta='Falar com a equipe técnica')}
    </div>
    <p class="plan-note">Clientes dos nossos Sistemas de Gestão têm condição própria, dentro do plano do sistema. O certificado digital A1 da empresa não está incluído: ele é emitido por uma certificadora de sua escolha e enviado ao CapyFiscal por um link seguro.</p>"""


def capyfiscal():
    curl = """<pre class="code"><span class="c"># 1. Envia a nota</span>
curl -u "<span class="s">SEU_TOKEN</span>:" -H "Content-Type: application/json" \\
  -X POST "https://api-fiscal.capycloud.com.br/v2/nfe?ref=<span class="s">venda-123</span>" \\
  -d @nota.json
<span class="c"># -&gt; 202 {"ref": "venda-123", "status": "processando_autorizacao"}</span>

<span class="c"># 2. Consulta a situação (ou aguarda o aviso por webhook)</span>
curl -u "<span class="s">SEU_TOKEN</span>:" https://api-fiscal.capycloud.com.br/v2/nfe/<span class="s">venda-123</span>
<span class="c"># -&gt; {"status": "autorizado", "chave_nfe": "NFe...", "caminho_danfe": "/arquivos/.../danfe.pdf"}</span></pre>"""
    return f"""
{hero_orig('Nota fiscal direto do seu <span class="text-capy-copper">sistema</span>', "Uma API de emissão de NF-e. O seu sistema envia os dados da venda, o CapyFiscal assina com o certificado da sua empresa, conversa com a SEFAZ e devolve o XML autorizado e o DANFE. Cancelamento, carta de correção e inutilização passam pelo mesmo lugar, sem você virar contador.", "Capivara emitindo NF-e e DANFE no notebook", "visao", "img/capyfiscal.webp", (1227, 1014))}

<section class="sec" id="como-funciona">
  <div class="wrap">
    <div class="mb-10">
      <h2>Como funciona</h2>
    </div>
    <div class="steps">
      <div class="step"><h3>A empresa é cadastrada uma vez</h3><p>Cadastramos o CNPJ, os dados fiscais e a numeração da sua empresa. O certificado digital A1 é enviado por um link seguro. Em geral, tudo fica pronto em um dia útil.</p></div>
      <div class="step"><h3>O seu sistema envia a venda</h3><p>O seu sistema manda os dados do cliente, dos produtos e dos impostos. Antes de seguir para a SEFAZ, o CapyFiscal confere tudo para evitar rejeições.</p></div>
      <div class="step"><h3>A nota volta autorizada</h3><p>O seu sistema recebe o XML autorizado e o DANFE em PDF. Se a SEFAZ recusar a nota, o motivo vem explicado em português claro.</p></div>
    </div>
  </div>
</section>

<section class="sec sec-cream" id="para-quem">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4">
      <h2>Para quem é</h2>
      <p class="mt-4">O CapyFiscal nasceu dentro dos nossos Sistemas de Gestão e hoje atende três perfis de empresa.</p>
    </div>
    <div class="lg:col-span-8 grid gap-6 sm:grid-cols-3">
      <div><span class="ico-box">{ico('nfe')}</span><h3 class="mt-4">Lojas e comércios</h3><p class="mt-2">Que já usam um sistema de gestão e querem emitir a nota direto dele, sem redigitar em outro emissor.</p></div>
      <div><span class="ico-box">{ico('automacao')}</span><h3 class="mt-4">Empresas com sistema próprio</h3><p class="mt-2">Com software interno ou feito sob medida, que precisam só da parte fiscal, sem trocar o resto.</p></div>
      <div><span class="ico-box">{ico('rede')}</span><h3 class="mt-4">Software houses</h3><p class="mt-2">Que emitem notas para os próprios clientes e precisam de uma API estável, com suporte técnico de verdade.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="o-que-entra">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4 lg:sticky lg:top-28 self-start">
      <h2>O que vem incluído</h2>
      <p class="mt-4">Em todos os planos.</p>
    </div>
    <div class="lg:col-span-8 ledger">
      <div class="ledger-row"><span class="ico-box">{ico('nfe')}</span><div><h3>Emissão e eventos</h3><p>NF-e de saída e de entrada, cancelamento, carta de correção e inutilização de numeração. A numeração é controlada pelo CapyFiscal, sem pular nem repetir.</p></div></div>
      <div class="ledger-row"><span class="ico-box">{ico('webhook')}</span><div><h3>Avisos automáticos</h3><p>O seu sistema é avisado sempre que a nota muda de situação. Se ele estiver fora do ar, o aviso é reenviado depois.</p></div></div>
      <div class="ledger-row"><span class="ico-box">{ico('pdf')}</span><div><h3>XML e DANFE por 5 anos</h3><p>Os arquivos ficam guardados pelo prazo legal, com download a qualquer momento e um pacote mensal pronto para o contador.</p></div></div>
      <div class="ledger-row"><span class="ico-box">{ico('chave')}</span><div><h3>Certificado digital protegido</h3><p>O certificado A1 é enviado por um link seguro e usado só para assinar as notas da sua empresa. Você recebe um aviso 30 e 7 dias antes de ele vencer.</p></div></div>
      <div class="ledger-row"><span class="ico-box">{ico('painel')}</span><div><h3>Painel na Área do Cliente</h3><p>Notas emitidas, situação de cada uma e motivos de rejeição, com o mesmo login da Área do Cliente da Capycloud.</p></div></div>
      <div class="ledger-row"><span class="ico-box">{ico('auditoria')}</span><div><h3>Conferência antes da SEFAZ</h3><p>CPF, CNPJ, município, CFOP e totais conferidos antes do envio, para a nota não voltar rejeitada.</p></div></div>
    </div>
  </div>
</section>

<section class="sec sec-cream" id="planos">
  <div class="wrap">
    {planos_capyfiscal()}
  </div>
</section>

<section class="sec" id="desenvolvedores">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-5">
      <h2>Para desenvolvedores</h2>
      <p class="lead mt-4">Uma API REST com JSON, no padrão de mercado para emissão de NF-e. Quem já integrou um provedor de nota fiscal adapta o sistema rapidamente.</p>
      <ul class="mt-6 space-y-3">
        <li class="flex gap-3">{ico('check','ico-copper')}<span>Autenticação por token</span></li>
        <li class="flex gap-3">{ico('check','ico-copper')}<span>Cada nota leva a referência do seu sistema, sem risco de emissão duplicada</span></li>
        <li class="flex gap-3">{ico('check','ico-copper')}<span>Ambientes separados de testes e de produção</span></li>
        <li class="flex gap-3">{ico('check','ico-copper')}<span>Documentação completa, com exemplos de cada chamada</span></li>
      </ul>
      <div class="mt-8 flex flex-wrap gap-3">
        <a class="btn btn-dark" href="capyfiscal-api.html">Abrir a documentação</a>
        <a class="btn btn-ghost" href="capyfiscal/openapi.yaml" download>Baixar o OpenAPI (YAML)</a>
      </div>
    </div>
    <div class="lg:col-span-7 min-w-0">{curl}</div>
  </div>
</section>

<section class="sec sec-cream" id="perguntas">
  <div class="wrap grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4"><h2>Perguntas frequentes</h2></div>
    <div class="lg:col-span-8 faq">
      <details><summary>Preciso trocar de contador?</summary><p>Não. Quem define CFOP, CST e alíquotas continua sendo o seu sistema, com os parâmetros que o seu contador já usa. O CapyFiscal cuida de emitir, guardar e enviar as notas.</p></details>
      <details><summary>E se a SEFAZ sair do ar?</summary><p>A nota fica na fila e é enviada sozinha quando o serviço volta. O seu sistema é avisado assim que ela for autorizada, sem risco de nota duplicada.</p></details>
      <details><summary>O meu certificado digital fica seguro?</summary><p>Sim. Ele é enviado por um link seguro, fica protegido e é usado só para assinar as notas que o seu sistema pedir. Isso está no contrato.</p></details>
      <details><summary>Posso testar antes de pagar?</summary><p>Sim. O ambiente de testes é liberado assim que a empresa é cadastrada e não tem limite de notas. As notas de teste não têm valor fiscal.</p></details>
      <details><summary>Uso um Sistema de Gestão da Capycloud. Preciso contratar à parte?</summary><p>Não. Nos nossos Sistemas de Gestão o CapyFiscal faz parte do plano e o botão Emitir já fica nas telas de venda e de entrada. Fale com o suporte para ativar.</p></details>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-box">
      <h2>Quer emitir pelo seu sistema?</h2>
      <p class="lead mx-auto mt-4">Diga qual sistema você usa e quantas notas emite por mês.</p>
      <div class="mt-8 flex flex-wrap justify-center gap-3">
        <a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener noreferrer">{ico('whatsapp')} Falar no WhatsApp</a>
        <a class="btn btn-dark" href="faleconosco.html">Outras formas de contato</a>
      </div>
    </div>
  </div>
</section>
"""


def capyfiscal_api():
    head = """<link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui.css">
  <style>.swagger-ui .topbar{display:none}.swagger-ui{font-family:inherit}.swagger-ui .info .title{color:#2D2926}</style>"""
    body = f"""
<section class="sec-cream">
  <div class="wrap py-10 lg:py-14 grid gap-6 lg:grid-cols-12 items-end">
    <div class="lg:col-span-8">
      <p class="kicker">CapyFiscal</p>
      <h1>Documentação da API</h1>
      <p class="lead mt-4">Referência completa das rotas, campos e respostas da API do CapyFiscal, com os endereços de produção e de testes.</p>
    </div>
    <div class="lg:col-span-4 flex flex-wrap gap-3 lg:justify-end">
      <a class="btn btn-ghost" href="capyfiscal/openapi.yaml" download>Baixar OpenAPI (YAML)</a>
      <a class="btn btn-gold" href="capyfiscal.html#planos">Planos</a>
    </div>
  </div>
</section>
<section class="py-6">
  <div class="wrap">
    <div id="swagger-ui"></div>
    <noscript><p>A documentação interativa precisa de JavaScript. Baixe o arquivo OpenAPI em <a href="capyfiscal/openapi.yaml">capyfiscal/openapi.yaml</a>.</p></noscript>
  </div>
</section>
<script src="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui-bundle.js" crossorigin></script>
<script>
  window.addEventListener('load', function () {{
    window.ui = SwaggerUIBundle({{ url: 'capyfiscal/openapi.yaml', dom_id: '#swagger-ui', deepLinking: true, docExpansion: 'list',
      defaultModelsExpandDepth: 0, tryItOutEnabled: false, supportedSubmitMethods: [] }});
  }});
</script>
"""
    return head, body


# ------------------------------------------------------------------ PLANOS
def _plan(nome, quem, preco, itens, hi=False, de=None, sufixo="/mês", nota=None, cta="Falar com a equipe", href="faleconosco.html"):
    lis = "".join(f"<li>{ico('check')}<span>{i}</span></li>" for i in itens)
    riscado = "" if de is None else (f"<s>R$ {de}</s>" if de else '<s class="vazio" aria-hidden="true">&nbsp;</s>')
    preco_html = f'<div class="price">{riscado}<strong>{preco}</strong><span>{sufixo}</span></div>'
    nota_html = f'<p class="price-note">{nota}</p>' if nota else ""
    return f"""
      <div class="plan{' plan-hi' if hi else ''}">
        <h3>{nome}</h3><p class="who">{quem}</p>
        {preco_html}{nota_html}
        <ul>{lis}</ul>
        <a class="btn btn-gold" href="{href}">{cta}</a>
      </div>"""


def planos():
    return f"""
{hero_orig('Planos e <span class="text-capy-copper">preços</span>', "O que tem preço fixo aparece aqui com o valor. O que depende do seu ambiente, como suporte, rede e site sob medida, aparece com o que está incluído e a forma de cobrança, e o valor sai depois de uma conversa. Nos dois casos, sem surpresa no fim do mês.", "Planos da Capycloud")}
<div class="wrap"><nav class="plan-nav" aria-label="Seções de planos">
  <a href="#cloud">Cloud privada</a><a href="#capyfiscal">CapyFiscal</a><a href="#hospedagem">Hospedagem e VPS</a><a href="#sites">Sites</a><a href="#manutencao">Manutenção remota</a><a href="#sistemas-de-gestao">Sistemas de Gestão</a>
</nav></div>

<section class="sec" id="cloud">
  <div class="wrap">
    <div class="mb-10">
      <h2>Cloud privada gerenciada</h2>
      <p class="lead mt-4">Infraestrutura dedicada, backup automático e suporte com prazo. A diferença entre os planos está no tamanho da equipe, nos chamados incluídos e na velocidade de resposta.</p>
    </div>
    <div class="plans plans-5">
      {_plan('CapyLight', 'Até 2 usuários', 'R$ 899', ['100 GB de armazenamento', 'Servidor de arquivos centralizado', 'Acesso remoto por VPN', 'Backup diário', 'Monitoramento básico', 'Até 2 chamados por mês', 'Resposta em até 8h úteis'], de='')}
      {_plan('CapyEssential', 'Até 5 usuários', 'R$ 999', ['200 GB de armazenamento', 'Servidor de arquivos centralizado', 'Acesso remoto por VPN', 'Usuários e permissões básicas', 'Backup diário', 'Monitoramento básico', 'Até 5 chamados por mês', 'Resposta em até 8h úteis'], de='1.199')}
      {_plan('CapyPro', 'Até 15 usuários', 'R$ 1.799', ['500 GB de armazenamento', 'Tudo do CapyEssential', 'Backup com versões anteriores', 'Grupos e políticas de acesso', 'Monitoramento com alertas', 'Relatórios básicos', 'Até 15 chamados por mês', 'Resposta em até 4h úteis'], hi=True, de='1.999')}
      {_plan('CapyElite', 'Até 30 usuários', 'R$ 2.599', ['1 TB de armazenamento', 'Tudo do CapyPro', 'Controle avançado de acessos', 'Auditoria de segurança', 'Prioridade no atendimento', 'Até 30 chamados por mês', 'Resposta em até 1h útil'], de='2.999')}
      {_plan('CapyEnterprise', 'Até 30 usuários', 'R$ 3.599', ['1 TB de armazenamento', 'Tudo do CapyElite', 'Chamados sem limite (uso justo)', 'Prioridade máxima na fila', 'Atendimento emergencial', 'Resposta em até 1h útil'], de='4.599')}
    </div>
    <p class="plan-note">Armazenamento e usuários extras sob demanda. Os planos cobrem o ambiente que a Capycloud gerencia; os equipamentos do seu escritório são avaliados à parte. A implantação é cobrada uma única vez, conforme o tamanho da migração.</p>
  </div>
</section>

<section class="sec sec-cream" id="capyfiscal">
  <div class="wrap">
    {_planos_cf()}
  </div>
</section>

<section class="sec" id="hospedagem">
  <div class="wrap">
    <div class="mb-10">
      <h2>Hospedagem gerenciada e VPS</h2>
      <p class="lead mt-4">Um servidor virtual para o seu sistema, a sua loja virtual ou um software de terceiros. A diferença é que a gente instala, atualiza, monitora e faz o backup: você usa, a Capycloud cuida.</p>
    </div>
    <div class="plans plans-4">
      {_plan('Hospedagem de site', 'Sites e landing pages', 'R$ 49', ['Hospedagem do site com certificado de segurança', 'Backup semanal', 'Monitoramento de disponibilidade', 'E-mail de aviso se o site cair', 'Domínio e DNS configurados'])}
      {_plan('VPS 1', 'Até 10 usuários', 'R$ 149', ['2 vCPU, 4 GB de memória, 60 GB SSD', 'Instalação do seu sistema ou aplicação', 'Atualizações de segurança do servidor', 'Backup diário com 7 dias de retenção', 'Monitoramento em horário comercial'])}
      {_plan('VPS 2', 'Até 30 usuários', 'R$ 249', ['4 vCPU, 8 GB de memória, 120 GB SSD', 'Tudo do VPS 1', 'Backup diário com 30 dias de retenção', 'Cópia do backup fora do servidor', 'Banco de dados gerenciado (PostgreSQL ou MySQL)'], hi=True)}
      {_plan('VPS 3', 'Várias aplicações', 'R$ 449', ['8 vCPU, 16 GB de memória, 240 GB SSD', 'Tudo do VPS 2', 'Ambiente de testes separado', 'Monitoramento com alertas 24h', 'Relatório mensal de uso e disponibilidade'])}
    </div>
    <p class="plan-note">Precisa de mais recursos ou de uma configuração específica (Windows, GPU, licenças)? Montamos sob medida. Tráfego e armazenamento extras sob demanda. A migração do seu sistema atual é orçada à parte, conforme a complexidade.</p>
  </div>
</section>

<section class="sec sec-cream" id="sites">
  <div class="wrap">
    <div class="mb-10">
      <h2>Sites</h2>
      <p class="lead mt-4">Três serviços diferentes: a landing page, uma página só, com preço de entrada; o site institucional, com várias páginas e valor conforme o projeto; e o cuidado mensal de um site que já existe.</p>
    </div>
    <div class="plans plans-3">
      {_plan('Landing page', 'Uma página, direta ao ponto', 'a partir de R$ 299', ['Uma página com a sua oferta e os seus contatos', 'Textos escritos junto com você', 'Pronta para celular e para o Google', 'Botão e formulário que levam ao seu WhatsApp'], sufixo='', nota='Projeto fechado; hospedagem à parte', cta='Quero uma landing page')}
      {_plan('Site institucional', 'Várias páginas', 'Sob orçamento', ['Início, quem somos, serviços, contato e o que mais a empresa precisar', 'Textos escritos junto com você', 'Pronto para celular e para o Google', 'Formulário que leva ao seu WhatsApp', 'Entrega em até 15 dias úteis depois do conteúdo aprovado'], sufixo='', nota='Valor conforme o número de páginas e os recursos', cta='Pedir orçamento')}
      {_plan('Manutenção de site', 'Para o site que você já tem', 'R$ 149', ['Até 2 horas por mês de alterações (textos, fotos, páginas)', 'Atualizações de segurança e da plataforma', 'Backup semanal e restauração quando precisar', 'Monitoramento de disponibilidade e do certificado', 'Hospedagem incluída se o site vier para a Capycloud'], hi=True, nota='Para sites em WordPress, HTML ou outras plataformas; avaliamos o site antes de fechar')}
    </div>
    <p class="plan-note">Lojas virtuais, portais e sistemas com login são orçados à parte.</p>
  </div>
</section>

<section class="sec" id="manutencao">
  <div class="wrap">
    <div class="mb-10">
      <h2>Manutenção remota mensal</h2>
      <p class="lead mt-4">A Capycloud passa a ser a TI da sua empresa por uma mensalidade. Você abre o chamado pelo WhatsApp ou pela Área do Cliente, o atendimento remoto acontece em horário comercial e, quando o remoto não resolve, a gente vai até você.</p>
      <p class="lead mt-4">O valor depende de quantos computadores e sistemas vamos cuidar e de como o ambiente está organizado hoje. Por isso, a primeira visita é um diagnóstico gratuito, que vira a proposta.</p>
    </div>
    <div class="min-w-0">
      <div class="table-wrap"><table class="compare">
        <thead><tr><th>O que está incluído</th><th>Até 5 computadores</th><th>Até 15 computadores</th><th>Até 30 computadores</th></tr></thead>
        <tbody>
          <tr><th scope="row">Atendimento remoto por mês</th><td>4 horas</td><td>8 horas</td><td>16 horas</td></tr>
          <tr><th scope="row">Tempo de resposta</th><td>Até 8 horas úteis</td><td>Até 4 horas úteis</td><td>Até 2 horas úteis</td></tr>
          <tr><th scope="row">Visita presencial</th><td>Cobrada por visita</td><td>1 por mês</td><td>2 por mês</td></tr>
          <tr><th scope="row">Emergência fora do horário</th><td>Cobrada à parte</td><td>Cobrada à parte</td><td>Incluída</td></tr>
          <tr><th scope="row">Manutenção preventiva</th><td>Trimestral</td><td>Mensal</td><td>Mensal</td></tr>
          <tr><th scope="row">Inventário e relatório mensal</th><td>Incluído</td><td>Incluído</td><td>Incluído</td></tr>
        </tbody>
        <tfoot><tr><th scope="row">Valor</th><td><strong>A partir de R$&nbsp;299/mês</strong></td><td>Sob proposta</td><td>Sob proposta</td></tr></tfoot>
      </table></div>
      <p class="plan-note">Horas excedentes e visitas avulsas têm valor fixo, definido em contrato. Impressoras, telefonia e softwares de terceiros entram no atendimento quando o fabricante permite suporte remoto.</p>
    </div>
  </div>
</section>

<section class="sec sec-cream" id="sistemas-de-gestao">
  <div class="wrap grid gap-8 lg:grid-cols-12 items-center">
    <div class="lg:col-span-7">
      <h2>Sistemas de Gestão</h2>
      <p class="lead mt-4">Sistemas prontos para o seu ramo: estoque, vendas, contratos e nota fiscal pelo CapyFiscal, com suporte remoto incluído no plano. Valor conforme o sistema e o tamanho da operação.</p>
    </div>
    <div class="lg:col-span-5 flex lg:justify-end">
      <a class="btn btn-dark" href="faleconosco.html">Falar com a equipe</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-box">
      <h2>Não cabe em nenhum plano?</h2>
      <p class="lead mx-auto mt-4">Conte o que precisa e a gente monta.</p>
      <div class="mt-8 flex flex-wrap justify-center gap-3">
        <a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener noreferrer">{ico('whatsapp')} Conversar no WhatsApp</a>
        <a class="btn btn-dark" href="faleconosco.html">Falar com a equipe</a>
      </div>
    </div>
  </div>
</section>
"""


def _planos_cf():
    return planos_capyfiscal(com_titulo=True)
