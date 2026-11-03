# Partes comuns do site: head, header com menu (e submenu do CapyFiscal), rodapé, sprite de ícones.
# Os ícones são desenhados à mão no "estilo nó": traço cobre + pontos dourados nos vértices,
# o mesmo motivo de rede que aparece nos mascotes.

SITE = "https://capycloud.com.br"
TEL_FMT = "(61) 98259-7571"
TEL_E164 = "5561982597571"
EMAIL = "contato@capycloud.com.br"
WA = f"https://wa.me/{TEL_E164}"
WA_MSG = f"{WA}?text=" + "Ol%C3%A1%2C%20quero%20conversar%20sobre%20os%20servi%C3%A7os%20da%20Capycloud."

TAILWIND_CFG = """<script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = { theme: { extend: {
      colors: { capy: {
        cream: '#EDE4D7', warm: '#E5D2BC', cool: '#D8C4AE', white: '#FFFFFF',
        copper: '#B07340', copperLight: '#C88A58', copperDark: '#8B5C32',
        gold: '#C49A42', goldHover: '#A87530', brown: '#8B6914',
        dark: '#2D2926', footer: '#161410', text: '#4D4033', muted: '#8A7B68',
        borderLight: '#C0AD95', borderCard: '#D2BFA8',
        purple: '#7B5EA7', green: '#5BAD7E', coral: '#E07A5F', sec: '#B85C38', maint: '#6B8E4A' } },
      fontFamily: { bulo: ['Bulo', 'system-ui', 'sans-serif'] },
      maxWidth: { prose2: '38rem' }
    } } }
  </script>"""

# ---------------------------------------------------------------------------------------------
# Sprite de ícones (viewBox 24). Classe .n = nó dourado. Uso: <svg class="ico"><use href="#i-xxx"/></svg>
# ---------------------------------------------------------------------------------------------
ICONS = {
 "arquivos": '<path d="M3.5 7.5v10a1.5 1.5 0 0 0 1.5 1.5h14a1.5 1.5 0 0 0 1.5-1.5V9.5a1.5 1.5 0 0 0-1.5-1.5h-7l-2-2.5H5a1.5 1.5 0 0 0-1.5 1.5Z"/><path d="M8 13.5h8M8 16h5"/><circle class="n" cx="19" cy="5" r="1.6"/>',
 "vpn": '<path d="M12 3.5 5 6.2v5.3c0 4.1 2.9 7.2 7 8.5 4.1-1.3 7-4.4 7-8.5V6.2L12 3.5Z"/><path d="M12 9.5v4"/><circle class="n" cx="12" cy="15.2" r="1.4"/>',
 "usuarios": '<circle cx="9" cy="8.5" r="3"/><path d="M3.5 19c0-3 2.5-5 5.5-5s5.5 2 5.5 5"/><path d="M15.5 5.8a3 3 0 0 1 0 5.4"/><path d="M17 14.3c2 .6 3.5 2.4 3.5 4.7"/><circle class="n" cx="16.5" cy="8.5" r="1.2"/>',
 "backup": '<ellipse cx="11" cy="6.5" rx="6.5" ry="2.5"/><path d="M4.5 6.5v9c0 1.4 2.9 2.5 6.5 2.5"/><path d="M17.5 6.5V11"/><path d="M15.5 16.5h5m0 0-2-2m2 2-2 2"/><circle class="n" cx="19.5" cy="11.5" r="1.5"/>',
 "monitor": '<rect x="3" y="4.5" width="18" height="12" rx="1.8"/><path d="M6.5 11.5h2.5l1.5-3 2 6 1.5-3h3.5"/><path d="M9 20h6M12 16.5V20"/><circle class="n" cx="17.5" cy="11.5" r="1.2"/>',
 "host": '<rect x="4" y="4" width="16" height="6" rx="1.5"/><rect x="4" y="14" width="16" height="6" rx="1.5"/><path d="M7.5 7h.01M7.5 17h.01"/><circle class="n" cx="16.5" cy="7" r="1.2"/><circle class="n" cx="16.5" cy="17" r="1.2"/>',
 "firewall": '<path d="M4 6h16M4 10h16M4 14h16M4 18h16"/><path d="M4 6v12M20 6v12M9 6v4M15 6v4M12 10v4M7 14v4M17 14v4"/><circle class="n" cx="12" cy="10" r="1.3"/>',
 "suporte": '<path d="M5 13v-2a7 7 0 0 1 14 0v2"/><rect x="3.5" y="12" width="4" height="6" rx="1.5"/><rect x="16.5" y="12" width="4" height="6" rx="1.5"/><path d="M18.5 18v1a2 2 0 0 1-2 2H13"/><circle class="n" cx="12" cy="21" r="1.2"/>',
 "auditoria": '<rect x="5.5" y="4" width="13" height="16" rx="1.8"/><path d="M9 3.5h6v2H9z"/><path d="m8.5 12.5 2 2 4.5-4.5"/><path d="M8.5 17h7"/><circle class="n" cx="18.5" cy="9" r="1.3"/>',
 "seguranca": '<path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"/><circle cx="12" cy="12" r="3"/><circle class="n" cx="12" cy="12" r="1.2"/>',
 "manutencao": '<path d="M14.5 6.5a4 4 0 0 0 4.9 4.9l-7.9 7.9a2 2 0 0 1-2.8-2.8l7.9-7.9a4 4 0 0 0-2.1-2.1Z"/><path d="M15 3.5a4.5 4.5 0 0 1 5.5 5.5"/><circle class="n" cx="6.2" cy="17.8" r="1.2"/>',
 "rede": '<circle cx="12" cy="5.5" r="2"/><circle cx="5" cy="17" r="2"/><circle cx="19" cy="17" r="2"/><path d="m10.8 7.2-4.6 7.9M13.2 7.2l4.6 7.9M7 17h10"/><circle class="n" cx="12" cy="5.5" r="1"/><circle class="n" cx="5" cy="17" r="1"/><circle class="n" cx="19" cy="17" r="1"/>',
 "cabo": '<path d="M4 12h5M15 12h5"/><rect x="9" y="8.5" width="6" height="7" rx="1.5"/><path d="M11 8.5V6M13 8.5V6M11 18v-2.5M13 18v-2.5"/><circle class="n" cx="4" cy="12" r="1.3"/><circle class="n" cx="20" cy="12" r="1.3"/>',
 "automacao": '<path d="M19.5 12a7.5 7.5 0 0 1-12.8 5.3M4.5 12A7.5 7.5 0 0 1 17.3 6.7"/><path d="M17.3 3.5v3.2h-3.2M6.7 20.5v-3.2h3.2"/><circle cx="12" cy="12" r="2.2"/><circle class="n" cx="12" cy="12" r="1"/>',
 "nfe": '<path d="M6.5 3.5h7l4 4V20a1 1 0 0 1-1 1h-10a1 1 0 0 1-1-1V4.5a1 1 0 0 1 1-1Z"/><path d="M13.5 3.5v4h4"/><path d="M9 11h6M9 14h6M9 17h3.5"/><circle class="n" cx="16" cy="17.5" r="1.4"/>',
 "site": '<rect x="3" y="4.5" width="18" height="15" rx="1.8"/><path d="M3 8.5h18"/><path d="M6.5 6.5h.01M9 6.5h.01"/><path d="M6.5 12h7M6.5 15h4.5"/><circle class="n" cx="16.5" cy="14" r="1.6"/>',
 "vps": '<path d="m12 3.5 7.5 4.3v8.4L12 20.5l-7.5-4.3V7.8L12 3.5Z"/><path d="M12 12 4.5 7.8M12 12l7.5-4.2M12 12v8.5"/><circle class="n" cx="12" cy="12" r="1.3"/>',
 "remoto": '<rect x="4" y="6" width="13" height="9" rx="1.5"/><path d="M2.5 18.5h16"/><path d="M19.5 7.5a3.5 3.5 0 0 1 0 5M21.5 5.5a6.5 6.5 0 0 1 0 9"/><circle class="n" cx="10.5" cy="10.5" r="1.3"/>',
 "celular": '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M11 17.5h2"/><circle class="n" cx="12" cy="9" r="1.3"/>',
 "email": '<rect x="3" y="5.5" width="18" height="13" rx="1.8"/><path d="m3.5 7 8.5 6 8.5-6"/><circle class="n" cx="12" cy="13" r="1.2"/>',
 "whatsapp": '<path d="M4 20l1.3-4A8 8 0 1 1 8.3 18.9L4 20Z"/><path d="M9.3 9.2c.2 2.6 2.5 5 5.4 5.4l1-1.5-2-1-1 .8a4.7 4.7 0 0 1-1.8-1.9l.8-1-1-2-1.4 1.2Z"/>',
 "telegram": '<path d="m3.5 11.5 16.5-7-3 15.5-5-3.5-2.5 2.5v-4l7.5-7-9.5 5.5-4-2Z"/>',
 "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
 "mais": '<path d="M12 5v14M5 12h14"/>',
 "relogio": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/><circle class="n" cx="12" cy="12" r="1"/>',
 "chave": '<circle cx="8" cy="12" r="3.5"/><path d="M11.5 12h9M17.5 12v3M20.5 12v2.5"/><circle class="n" cx="8" cy="12" r="1.2"/>',
 "pasta5": '<path d="M4 7h5l2 2h9v10H4z"/><path d="M8 13h8"/><circle class="n" cx="16" cy="16" r="1.3"/>',
 "webhook": '<path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 2h-14z"/><path d="M10 20.5a2 2 0 0 0 4 0"/><circle class="n" cx="17.5" cy="6" r="1.6"/>',
 "pdf": '<rect x="3.5" y="4" width="17" height="4.5" rx="1"/><path d="M5 8.5v10a1.5 1.5 0 0 0 1.5 1.5h11a1.5 1.5 0 0 0 1.5-1.5v-10"/><path d="M10 12.5h4"/><circle class="n" cx="12" cy="16.5" r="1.2"/>',
 "painel": '<rect x="3" y="4" width="18" height="16" rx="1.8"/><path d="M3 9h18M8 9v11"/><circle class="n" cx="14.5" cy="14.5" r="1.4"/>',
 "mapa": '<path d="m3.5 6 5.5-2 6 2 5.5-2v14l-5.5 2-6-2-5.5 2V6Z"/><path d="M9 4v14M15 6v14"/><circle class="n" cx="12" cy="11" r="1.3"/>',
 "visita": '<path d="M12 21s-6-5.5-6-10.5a6 6 0 0 1 12 0C18 15.5 12 21 12 21Z"/><circle cx="12" cy="10.5" r="2.2"/><circle class="n" cx="12" cy="10.5" r=".9"/>',
 "alvo": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle class="n" cx="12" cy="12" r="1.4"/>',
 "camadas": '<path d="m12 4 8 4-8 4-8-4 8-4Z"/><path d="m4 12 8 4 8-4M4 16l8 4 8-4"/><circle class="n" cx="12" cy="8" r="1"/>',
}


def sprite() -> str:
    syms = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">{syms}</svg>'


def ico(nome: str, cls: str = "") -> str:
    return f'<svg class="ico {cls}" aria-hidden="true"><use href="#i-{nome}"/></svg>'


# ---------------------------------------------------------------------------------------------
# Menu. "ativo" é o nome da página (index, servicos, capyfiscal, planos, quemsomos, faleconosco, area)
# ---------------------------------------------------------------------------------------------
MENU = [
    ("index", "index.html", "Início"),
    ("quemsomos", "quemsomos.html", "Quem Somos"),
    ("servicos", "servicos.html", "Serviços"),
    ("capyfiscal", "capyfiscal.html", "CapyFiscal"),
    ("planos", "planos.html", "Planos"),
    ("faleconosco", "faleconosco.html", "Contato"),
]
SUBMENU_CAPYFISCAL = [
    ("capyfiscal.html#visao", "Visão geral"),
    ("capyfiscal.html#como-funciona", "Como funciona"),
    ("capyfiscal.html#para-quem", "Para quem é"),
    ("capyfiscal.html#planos", "Planos e preços"),
    ("capyfiscal.html#desenvolvedores", "Para desenvolvedores"),
    ("capyfiscal-api.html", "Documentação da API"),
    ("capyfiscal.html#perguntas", "Perguntas frequentes"),
]


def header(ativo: str) -> str:
    itens = []
    for chave, href, rotulo in MENU:
        cls = "nav-link" + (" is-active" if chave == ativo else "")
        if chave == "capyfiscal":
            sub = "".join(f'<a href="{h}">{r}</a>' for h, r in SUBMENU_CAPYFISCAL)
            itens.append(
                f'<div class="nav-drop"><a href="{href}" class="{cls}">{rotulo}<span class="caret" aria-hidden="true"></span></a>'
                f'<div class="nav-drop-panel" role="menu">{sub}</div></div>')
        else:
            itens.append(f'<a href="{href}" class="{cls}">{rotulo}</a>')
    desktop = "".join(itens)
    mob = "".join(
        f'<a href="{href}" class="mob-link{" is-active" if chave == ativo else ""}">{rotulo}</a>'
        + ("".join(f'<a href="{h}" class="mob-sub">{r}</a>' for h, r in SUBMENU_CAPYFISCAL) if chave == "capyfiscal" else "")
        for chave, href, rotulo in MENU)
    area_cls = "btn-area" + (" is-active" if ativo == "area" else "")
    return f"""
  <header class="site-header">
    <div class="wrap header-row">
      <a href="index.html" class="logo" aria-label="Capycloud, início"><span class="logo-a">Capy</span><span class="logo-b">cloud</span></a>
      <nav class="nav-desktop" aria-label="Principal">{desktop}
        <a href="area-do-cliente.html" class="{area_cls}">Área do Cliente</a>
      </nav>
      <button id="mobile-menu-btn" class="menu-btn" aria-expanded="false" aria-controls="mobile-menu" aria-label="Abrir menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div id="mobile-menu" class="mobile-menu" hidden>
      {mob}
      <a href="area-do-cliente.html" class="mob-link mob-area">Área do Cliente</a>
    </div>
  </header>"""


def footer() -> str:
    return f"""
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <a href="index.html" class="logo logo-footer"><span class="logo-a">Capy</span><span class="logo-b">cloud</span></a>
        <p class="footer-tag">Infraestrutura, sistemas e suporte para empresas que preferem ter alguém para chamar.</p>
        <p class="footer-contact">
          <a href="mailto:{EMAIL}">{ico('email')} {EMAIL}</a>
          <a href="tel:+{TEL_E164}">{ico('celular')} {TEL_FMT}</a>
        </p>
      </div>
      <div class="footer-col">
        <h4>Serviços</h4>
        <a href="servicos.html#infraestrutura">Cloud privada gerenciada</a>
        <a href="servicos.html#sistemas">Sistemas e automação</a>
        <a href="servicos.html#suporte">Suporte técnico e manutenção</a>
        <a href="servicos.html#redes">Rede do escritório</a>
        <a href="servicos.html#sites">Sites e hospedagem</a>
      </div>
      <div class="footer-col">
        <h4>CapyFiscal</h4>
        <a href="capyfiscal.html">Visão geral</a>
        <a href="capyfiscal.html#planos">Planos e preços</a>
        <a href="capyfiscal-api.html">Documentação da API</a>
        <a href="capyfiscal.html#perguntas">Perguntas frequentes</a>
      </div>
      <div class="footer-col">
        <h4>Capycloud</h4>
        <a href="quemsomos.html">Quem somos</a>
        <a href="planos.html">Planos</a>
        <a href="faleconosco.html">Contato</a>
        <a href="area-do-cliente.html">Área do Cliente</a>
        <a href="privacidade.html">Política de privacidade</a>
      </div>
    </div>
    <div class="wrap footer-base">
      <span>© 2026 Capycloud. Todos os direitos reservados.</span>
      <span>Asa Sul, Brasília, DF</span>
    </div>
  </footer>"""


def page(*, slug: str, ativo: str, title: str, desc: str, body: str, og_image: str = "img/capyaba-software.webp",
         extra_head: str = "", noindex: bool = False, body_class: str = "") -> str:
    canonical = f"{SITE}/{slug}" if slug != "index.html" else f"{SITE}/"
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  {robots}
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/{og_image}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Capycloud">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#EDE4D7">
  {TAILWIND_CFG}
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" type="image/png" sizes="64x64" href="img/capyaba.png">
  <link rel="apple-touch-icon" sizes="180x180" href="img/capyaba.png">
  {extra_head}
</head>
<body class="{body_class}">
  {sprite()}
  {header(ativo)}
  <main id="conteudo">
{body}
  </main>
  {footer()}
  <script src="js/main.js"></script>
</body>
</html>
"""
