"""Página de documentação da API do CapyFiscal (capyfiscal-api.html).

Mesma sequência de cores da página do CapyFiscal: começa no tom do rodapé e alterna com o creme.
O guia (processos) é HTML escrito aqui; a referência das rotas é o Swagger UI lendo capyfiscal/openapi.yaml.
"""

SWAGGER = "5.17.14"


def _status():
    linhas = [
        ("processando_autorizacao", "A nota foi recebida e está na fila ou em análise na SEFAZ. Aguarde o aviso."),
        ("autorizado", "Nota válida. Chave, protocolo, XML e DANFE já estão disponíveis."),
        ("erro_autorizacao", "A SEFAZ recusou a nota. O motivo vem em mensagem_sefaz. Corrija e envie de novo com a mesma referência."),
        ("denegado", "A SEFAZ negou o uso por irregularidade cadastral do emitente ou do destinatário. O número fica usado e a nota não pode ser reenviada."),
        ("cancelado", "A nota foi cancelada. O XML do cancelamento vem em caminho_xml_cancelamento."),
    ]
    return "".join(f"<tr><td><code>{s}</code></td><td>{t}</td></tr>" for s, t in linhas)


def _erros():
    linhas = [
        ("400", "requisicao_invalida", "Parâmetro ausente ou fora do formato, como a referência."),
        ("400", "nfe_nao_autorizada", "A operação exige uma nota autorizada."),
        ("401", "nao_autorizado", "Token ausente ou inválido."),
        ("401", "ambiente_incorreto", "Token de testes usado em produção, ou o contrário."),
        ("404", "nao_encontrado", "Nota, empresa, gatilho ou arquivo não encontrado."),
        ("415", "formato_invalido", "A requisição chegou sem corpo JSON."),
        ("422", "erro_validacao_schema", "Dados da nota inválidos. A lista erros traz cada campo."),
        ("422", "erro_validacao", "Dados da empresa inválidos. A lista erros traz cada campo."),
        ("422", "pending_operation", "A nota com essa referência ainda está em processamento."),
        ("422", "already_processed", "A nota com essa referência já foi autorizada, cancelada ou denegada."),
        ("422", "permissao_negada", "O CNPJ informado não pertence ao token, ou a empresa está desativada."),
        ("422", "certificado_ausente", "A empresa ainda não tem certificado digital cadastrado."),
        ("422", "limite_cartas", "A nota já tem 20 cartas de correção."),
        ("429", "limite_excedido", "Mais de 100 requisições por minuto com o mesmo token."),
    ]
    return "".join(f"<tr><td>{h}</td><td><code>{c}</code></td><td>{t}</td></tr>" for h, c, t in linhas)


def capyfiscal_api():
    head = f"""<link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@{SWAGGER}/swagger-ui.css">
  <link rel="stylesheet" href="css/capyfiscal-api.css">"""
    body = f"""
<section class="api-sec api-escura" id="topo">
  <div class="wrap py-6 lg:py-10 flex flex-col lg:flex-row items-center gap-10 lg:gap-16">
    <div class="w-full lg:w-5/12 flex justify-center">
      <img src="img/capyfiscal.webp" alt="Capivara emitindo NF-e e DANFE no notebook" class="w-full max-w-md lg:max-w-none fx-float" width="1227" height="1014">
    </div>
    <div class="w-full lg:w-7/12">
    <p class="kicker">CapyFiscal</p>
    <h1>Documentação da API</h1>
    <p class="lead mt-5">Tudo o que o seu sistema precisa para emitir NF-e pelo CapyFiscal: o caminho de uma nota, as situações, os erros, os avisos automáticos e a referência de cada rota.</p>
    <p class="api-aviso mt-5">O acesso é liberado depois do cadastro da empresa. Fale com a equipe para receber os tokens do ambiente de testes.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-gold" href="faleconosco.html">Pedir acesso</a>
      <a class="btn btn-claro" href="capyfiscal/openapi.yaml" download>Baixar OpenAPI (YAML)</a>
    </div>
    </div>
  </div>
</section>

<section class="api-sec api-creme" id="comecar">
  <div class="wrap">
    <h2>Antes de começar</h2>
    <div class="api-3 mt-8">
      <div>
        <h3>Endereços</h3>
        <p>Produção:<br><code>https://api-fiscal.capycloud.com.br/v2</code></p>
        <p class="mt-3">Testes (homologação), sem valor fiscal:<br><code>https://homologacao-fiscal.capycloud.com.br/v2</code></p>
      </div>
      <div>
        <h3>Autenticação</h3>
        <p>HTTP Basic com o token como usuário e senha em branco, ou <code>Authorization: Bearer TOKEN</code>.</p>
        <p class="mt-3">Cada empresa tem dois tokens, um de produção e um de testes. O token de integrador serve para cadastrar empresas.</p>
      </div>
      <div>
        <h3>Regras gerais</h3>
        <p>JSON em UTF-8 no envio e na resposta.</p>
        <p class="mt-3">Até 100 requisições por minuto por token.</p>
        <p class="mt-3">Cada nota leva uma referência sua, única por empresa: letras, números, <code>-</code> e <code>_</code>, até 64 caracteres.</p>
      </div>
    </div>
  </div>
</section>

<section class="api-sec api-escura" id="caminho">
  <div class="wrap">
    <h2>O caminho de uma nota</h2>
    <div class="steps mt-8">
      <div class="step"><h3>Envie a nota</h3><p><code>POST /v2/nfe?ref=venda-123</code> com os dados da venda. A resposta vem na hora, com <code>202</code> e a situação <code>processando_autorizacao</code>.</p></div>
      <div class="step"><h3>Receba o resultado</h3><p>O aviso automático chega no endereço que você cadastrou. Se preferir, consulte com <code>GET /v2/nfe/venda-123</code>.</p></div>
      <div class="step"><h3>Autorizada: guarde os arquivos</h3><p>A resposta traz a chave, o protocolo e os caminhos do XML e do DANFE, guardados por 5 anos.</p></div>
    </div>
    <div class="api-2 mt-12">
      <div>
        <h3>Se a SEFAZ recusar</h3>
        <p>A situação vira <code>erro_autorizacao</code> e o motivo vem em <code>mensagem_sefaz</code>. Corrija os dados e envie de novo com a mesma referência: ela vira uma nova tentativa da mesma nota.</p>
      </div>
      <div>
        <h3>Depois da autorização</h3>
        <p>Cancelamento com <code>DELETE /v2/nfe/venda-123</code>, em geral até 24 horas depois. Carta de correção com <code>POST /v2/nfe/venda-123/carta_correcao</code>, até 20 por nota. As duas respondem na hora, já com o resultado da SEFAZ.</p>
      </div>
    </div>
  </div>
</section>

<section class="api-sec api-creme" id="situacoes">
  <div class="wrap">
    <h2>Situações da nota</h2>
    <div class="table-wrap mt-8"><table class="api-tabela"><thead><tr><th>status</th><th>O que significa</th></tr></thead><tbody>{_status()}</tbody></table></div>
    <h2 class="mt-16">Erros</h2>
    <p class="lead mt-4">Todo erro volta no mesmo formato: <code>codigo</code>, <code>mensagem</code> e, nos erros de validação, a lista <code>erros</code> com o campo de cada problema.</p>
    <div class="table-wrap mt-8"><table class="api-tabela"><thead><tr><th>HTTP</th><th>codigo</th><th>Quando acontece</th></tr></thead><tbody>{_erros()}</tbody></table></div>
  </div>
</section>

<section class="api-sec api-escura" id="avisos">
  <div class="wrap api-2">
    <div>
      <h2>Avisos automáticos</h2>
      <p class="lead mt-4">Cadastre um endereço com <code>POST /v2/hooks</code> e o seu sistema recebe um <code>POST</code> sempre que uma nota é autorizada, recusada, denegada ou cancelada. O corpo é o mesmo da consulta.</p>
      <ul class="api-lista mt-6">
        <li>Responda com qualquer código 2xx para confirmar o recebimento.</li>
        <li>Sem resposta 2xx, o aviso é reenviado depois de 1 minuto, 30 minutos, 1 hora, 3 horas e 24 horas.</li>
        <li>Cada aviso traz os cabeçalhos <code>X-CapyFiscal-Event</code>, <code>X-CapyFiscal-Delivery</code> (identificador único) e <code>X-CapyFiscal-Signature</code>.</li>
        <li>Use o <code>X-CapyFiscal-Delivery</code> para ignorar um aviso repetido.</li>
      </ul>
    </div>
    <div class="min-w-0">
      <h3>Conferindo a assinatura</h3>
      <p class="mt-2">A assinatura é um HMAC-SHA256 do corpo, com o <code>segredo_hmac</code> devolvido no cadastro do endereço.</p>
      <pre class="code mt-4"><span class="c"># Python</span>
<span class="k">import</span> hmac, hashlib

assinatura = cabecalhos[<span class="s">"X-CapyFiscal-Signature"</span>]
calculada = hmac.new(SEGREDO.encode(), corpo_bruto,
                     hashlib.sha256).hexdigest()
valido = hmac.compare_digest(<span class="s">"sha256="</span> + calculada,
                             assinatura)</pre>
    </div>
  </div>
</section>

<section class="api-sec api-creme" id="referencia">
  <div class="wrap">
    <h2>Referência das rotas</h2>
    <p class="lead mt-4">Clique em uma rota para ver os parâmetros, o corpo esperado e os exemplos de resposta.</p>
    <div id="swagger-ui" class="mt-6"></div>
    <noscript><p>A referência interativa precisa de JavaScript. Baixe o arquivo <a href="capyfiscal/openapi.yaml">openapi.yaml</a>.</p></noscript>
  </div>
</section>


<script src="https://unpkg.com/swagger-ui-dist@{SWAGGER}/swagger-ui-bundle.js" crossorigin></script>
<script>
  /* Rótulos do Swagger em português */
  var TRADUCOES = {{
    'Parameters': 'Parâmetros', 'Responses': 'Respostas', 'Request body': 'Corpo da requisição', 'Description': 'Descrição',
    'Name': 'Nome', 'Code': 'Código', 'Example Value': 'Exemplo', 'Schema': 'Modelo', 'Schemas': 'Modelos de dados',
    'No parameters': 'Sem parâmetros', 'Media type': 'Tipo de conteúdo', 'Servers': 'Servidor', 'Links': '',
    'No links': '', 'required': 'obrigatório', 'Examples': 'Exemplos', 'Default value': 'Padrão', 'Available values': 'Valores aceitos',
    'Controls Accept header.': '', 'Expand all': 'Abrir todos', 'Collapse all': 'Fechar todos'
  }};
  function traduzir(raiz) {{
    var w = document.createTreeWalker(raiz, NodeFilter.SHOW_TEXT, null);
    var n; while ((n = w.nextNode())) {{
      var t = n.nodeValue.trim();
      if (t && Object.prototype.hasOwnProperty.call(TRADUCOES, t)) n.nodeValue = n.nodeValue.replace(t, TRADUCOES[t]);
      else if (/^Default value\\s*:/.test(t)) n.nodeValue = n.nodeValue.replace('Default value', 'Padrão');
    }}
    /* restrições dos campos ("maxLength: 60" etc.): o React parte o texto em pedaços, então traduz pelo elemento */
    var ROT = {{ 'maxLength': 'máximo de caracteres', 'minLength': 'mínimo de caracteres', 'default': 'padrão',
                 'maximum': 'máximo', 'minimum': 'mínimo', 'pattern': 'formato', 'nullable': 'pode ser nulo' }};
    raiz.querySelectorAll('.property.primitive').forEach(function (el) {{
      if (el.dataset.traduzido) return;
      var m = el.textContent.trim().match(/^(\\w+):\\s*(.*)$/);
      if (!m || !ROT[m[1]]) return;
      var texto = m[1] === 'nullable' ? ROT.nullable : ROT[m[1]] + ': ' + m[2];
      el.dataset.traduzido = '1';
      el.replaceChildren(document.createElement('br'), document.createTextNode(texto));
    }});
  }}
  window.addEventListener('load', function () {{
    var alvo = document.getElementById('swagger-ui');
    window.ui = SwaggerUIBundle({{
      url: 'capyfiscal/openapi.yaml', dom_id: '#swagger-ui', deepLinking: true, docExpansion: 'list',
      defaultModelsExpandDepth: -1, defaultModelExpandDepth: 2, tryItOutEnabled: false, supportedSubmitMethods: [],
      displayRequestDuration: false, filter: false, showExtensions: false,
      syntaxHighlight: {{ activated: true, theme: 'tomorrow-night' }}
    }});
    var agendado = false;
    new MutationObserver(function () {{ if (agendado) return; agendado = true; requestAnimationFrame(function () {{ agendado = false; traduzir(alvo); }}); }})
      .observe(alvo, {{ childList: true, subtree: true, characterData: true }});
  }});
</script>
"""
    return head, body
