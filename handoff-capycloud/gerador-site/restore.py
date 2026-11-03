# Casca do site ORIGINAL: head (tailwind.config), cabeçalho e menu idênticos ao que está no ar,
# só com o item CapyFiscal acrescentado no mesmo estilo dos outros. Rodapé novo (aprovado).
import re
from common import footer, sprite

TAILWIND_ORIG = """<script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: { capy: {
              cream: '#EDE4D7',
              warm: '#E5D2BC',
              cool: '#D8C4AE',
              white: '#FFFFFF',
              copper: '#B07340',
              copperLight: '#C88A58',
              copperDark: '#8B5C32',
              gold: '#C49A42',
              goldHover: '#A87530',
              brown: '#8B6914',
              dark: '#2D2926',
              footer: '#161410',
              text: '#4D4033',
              muted: '#8A7B68',
              borderLight: '#C0AD95',
              borderCard: '#D2BFA8',
              purple: '#7B5EA7',
              green: '#5BAD7E',
              coral: '#E07A5F',
              sec: '#B85C38',
              maint: '#6B8E4A',
            } }
        }
      }
    }
  </script>"""

FAVICONS_ANTIGO = """<!-- Favicon — CapyAlba -->
  <link rel="icon" type="image/png" sizes="64x64" href="img/capyaba.png">
  <link rel="icon" type="image/png" sizes="32x32" href="img/capyaba.png">
  <link rel="icon" type="image/png" sizes="16x16" href="img/capyaba.png">
  <link rel="icon" type="image/x-icon" href="img/capyaba.png">
  <link rel="apple-touch-icon" sizes="180x180" href="img/capyaba.png">"""

# Favicon novo: capivara com fundo transparente (gerada em 23/10). O .ico fica na raiz do site.
FAVICONS = """<!-- Favicon: capivara com fundo transparente -->
  <link rel="icon" href="favicon.ico" sizes="16x16 32x32 48x48">
  <link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="img/favicon-192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="img/apple-touch-icon.png">"""

BODY_ORIG = '<body class="bg-white text-capy-dark font-sans antialiased fx-grain">'

MENU_ORIG = [
    ("index", "index.html", "Início"),
    ("quemsomos", "quemsomos.html", "Quem Somos"),
    ("servicos", "servicos.html", "Serviços"),
    ("planos", "planos.html", "Planos"),
    ("faleconosco", "faleconosco.html", "Contato"),
    ("capyfiscal", "capyfiscal.html", "CapyFiscal"),
    ("area", "area-do-cliente.html", "Área do Cliente"),
]


def header_orig(ativo: str) -> str:
    desk, mob = [], []
    for chave, href, rotulo in MENU_ORIG:
        if chave == ativo:
            desk.append(f'          <a href="{href}" class="nav-link text-capy-copper transition-colors font-medium">{rotulo}</a>')
            mob.append(f'        <a href="{href}" class="block text-capy-copper py-2 font-medium">{rotulo}</a>')
        else:
            desk.append(f'          <a href="{href}" class="nav-link text-capy-text hover:text-capy-copper transition-colors font-medium">{rotulo}</a>')
            mob.append(f'        <a href="{href}" class="block text-capy-text hover:text-capy-copper py-2 font-medium">{rotulo}</a>')
    return f"""<!-- HEADER -->
  <header class="bg-capy-cream/90 backdrop-blur-md sticky top-0 z-50 border-b border-capy-borderLight">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <a href="index.html" class="flex-shrink-0 flex items-center cursor-pointer">
          <span class="text-3xl font-extrabold text-capy-copper tracking-tighter">Capy</span>
          <span class="text-3xl font-bold text-capy-dark tracking-tighter">cloud</span>
        </a>
        <nav class="hidden md:flex space-x-8">
{chr(10).join(desk)}
        </nav>
        <div class="md:hidden flex items-center">
          <button id="mobile-menu-btn" class="text-capy-text hover:text-capy-dark focus:outline-none p-2" aria-label="Menu">
            <svg class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="mobile-menu md:hidden bg-capy-cream/95 border-t border-capy-borderLight">
      <div class="px-4 py-4 space-y-3">
{chr(10).join(mob)}
      </div>
    </div>
  </header>"""


def aplicar_casca(html: str, ativo: str) -> str:
    """Pega uma página ORIGINAL e troca só: cabeçalho (menu com CapyFiscal), rodapé (novo) e injeta o sprite de ícones."""
    html, n1 = re.subn(r'<!-- HEADER[^>]*-->\s*<header.*?</header>', header_orig(ativo), html, count=1, flags=re.S)
    if n1 == 0:
        html, n1 = re.subn(r'<header.*?</header>', header_orig(ativo), html, count=1, flags=re.S)
    html, n2 = re.subn(r'<!-- FOOTER[^>]*-->\s*<footer.*?</footer>', footer().strip(), html, count=1, flags=re.S)
    if n2 == 0:
        html, n2 = re.subn(r'<footer.*?</footer>', footer().strip(), html, count=1, flags=re.S)
    html, n3 = re.subn(r'(<body[^>]*>)', r'\1\n  ' + sprite().replace('\\', '\\\\'), html, count=1)
    assert n1 == n2 == n3 == 1, (n1, n2, n3)
    assert html.count(FAVICONS_ANTIGO) == 1, "favicon antigo não encontrado"
    html = html.replace(FAVICONS_ANTIGO, FAVICONS)
    return html


def pagina_nova(*, slug, ativo, title, desc, body, extra_head="", noindex=False):
    """Páginas novas (Serviços, CapyFiscal, Planos...) com a mesma casca do site original."""
    SITE = "https://capycloud.com.br"
    canonical = f"{SITE}/{slug}"
    robots = '\n  <meta name="robots" content="noindex, nofollow">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">{robots}
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/img/capyaba-software.png">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Capycloud">
  <meta name="twitter:card" content="summary_large_image">
  <title>{title}</title>
  {TAILWIND_ORIG}
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/paginas-novas.css">

  {FAVICONS}
  {extra_head}
</head>
{BODY_ORIG}
  {sprite()}

  {header_orig(ativo)}

  <main>
{body}
  </main>

  {footer().strip()}

  <script src="js/main.js"></script>
</body>
</html>
"""
