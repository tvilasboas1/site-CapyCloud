# Capycloud, site institucional

Site estático: HTML + Tailwind (CDN) + `css/style.css` + `js/main.js`. Sem build. Publicado em https://capycloud.com.br.

## Páginas

| Arquivo | O que é |
|---|---|
| `index.html` | Início: cinco frentes de serviço, destaque do CapyFiscal, por que a Capycloud, contato |
| `servicos.html` | Portfólio completo em cinco frentes (cloud privada, sistemas e automação, suporte e manutenção, redes e cabeamento, sites e hospedagem). Cada serviço traz a forma de cobrar: mensalidade, orçamento após análise ou por projeto |
| `capyfiscal.html` | Página do produto CapyFiscal, com submenu no cabeçalho: visão geral, como funciona, para quem é, o que vem incluído, planos, para desenvolvedores, perguntas frequentes |
| `capyfiscal-api.html` | Documentação interativa da API (Swagger UI lendo `capyfiscal/openapi.yaml`). Só funciona servida por HTTP, não abrindo o arquivo direto no navegador |
| `planos.html` | Planos: cloud privada, CapyFiscal, hospedagem e VPS, sites, manutenção remota mensal, MotoGestor |
| `quemsomos.html`, `faleconosco.html`, `area-do-cliente.html`, `privacidade.html` | Institucionais |

## Como editar

- Menu, rodapé e ícones estão repetidos em cada página (não há include). Ao mudar o menu, mude em todas. O submenu do CapyFiscal é o bloco `nav-drop` no cabeçalho e os links `mob-sub` no menu móvel.
- Ícones: um sprite SVG inline no início de cada `<body>` (`<symbol id="i-nome">`). Para usar: `<svg class="ico"><use href="#i-nome"/></svg>`. Para criar um ícone novo, desenhe no mesmo estilo (traço 1.6, cantos arredondados, um ou mais pontos dourados `class="n"`) e copie o `symbol` para todas as páginas.
- Cores e fonte: `tailwind.config` no `<head>` de cada página e variáveis em `css/style.css`. Fonte Bulo em `fonts/`.
- Preços: estão escritos nos HTML (`planos.html` e `capyfiscal.html`; os planos do CapyFiscal aparecem nos dois lugares, mantenha iguais).
- Imagens: os mascotes têm versão `.webp` (30 a 70 KB) usada nas páginas; os `.png` originais (1 a 1,7 MB) ficam como fonte. Para novas imagens, gere o `.webp` antes de usar.
- Formulário de contato (`faleconosco.html`): monta a mensagem e abre o WhatsApp (número em `js/main.js`).

## Checklist antes de publicar

1. Abrir cada página no celular (largura 390 px) e conferir que não há rolagem horizontal.
2. `sitemap.xml` com a data da alteração.
3. Telefone: (61) 98259-7571 em todas as páginas e em `js/main.js`.
