"""Rodada 3 do site: volta ao original (casca, fonte, tamanhos), com cirurgias pontuais.

- index.html e quemsomos.html: partem do HTML ORIGINAL; troca só cabeçalho (menu + CapyFiscal), rodapé (novo)
  e, na index, os trechos que o Danylo pediu.
- demais páginas: conteúdo novo, mas com a casca original (mesmo head, menu, corpo, fonte).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import ico
from restore import aplicar_casca, pagina_nova
from pages_home_servicos import NODES_HERO, servicos
import pages_capyfiscal_planos as cp
import pages_outras as ot

ORIG = sys.argv[1]   # pasta do site original
OUT = sys.argv[2]    # pasta de saída


def troca(html, antigo, novo):
    assert html.count(antigo) == 1, antigo[:80]
    return html.replace(antigo, novo)


def card_link(href, icone, titulo, texto):
    return f"""
            <a class="front" href="{href}">{ico(icone)}<div><strong>{titulo}</strong><small>{texto}</small></div></a>"""


def card_razao(icone, titulo, texto):
    return f"""
        <div class="front">{ico(icone)}<div><strong>{titulo}</strong><small>{texto}</small></div></div>"""


def cta_sem_caixa(h, titulo_antigo, novo_p_regex, novo_p):
    """Tira a caixa marrom (fundo, borda, brilho) do bloco final e encurta o texto. Mantém título e botão."""
    h, n = re.subn(
        r'<div class="relative overflow-hidden rounded-3xl p-10 md:p-16 text-center bg-capy-warm border border-capy-gold/20 shadow-sm">\s*'
        r'<div class="absolute top-0[^"]*"\s*style="[^"]*">\s*</div>\s*<div class="relative z-10">',
        '<div class="text-center">\n        <div>', h, count=1)
    assert n == 1, "caixa do CTA não encontrada"
    h, n = re.subn(novo_p_regex, novo_p, h, count=1, flags=re.S)
    assert n == 1, "texto do CTA não encontrado"
    return h


def index():
    h = open(os.path.join(ORIG, "index.html"), encoding="utf-8").read()
    h = aplicar_casca(h, "index")

    # 1) Raios atrás do hero
    h = troca(h, "    <!-- Animações de fundo removidas para fundo branco limpo -->\n",
              "    <!-- Raios: rede de nós animada (css/style.css, bloco ACRÉSCIMOS) -->\n" + NODES_HERO + "\n")

    # 2) Texto do hero: o original, com os serviços novos citados em uma palavra cada
    h = troca(h,
        "cuida de toda a infraestrutura: Arquivos centralizados, backups automáticos, acessos controlados e segurança gerenciada. Tudo com",
        "cuida de toda a infraestrutura: Arquivos centralizados, backups automáticos, acessos controlados e segurança gerenciada. E também de suporte, redes, sites, automações e nota fiscal. Tudo com")

    # 3) Ecossistema: mesmo layout; texto sem "Software Livre"; quadradinhos com link para cada frente
    h = troca(h,
        "Soluções integradas que trabalham juntas. Infraestrutura própria, gerenciada por especialistas, construída sobre Software Livre.",
        "Soluções integradas que trabalham juntas: infraestrutura, sistemas, suporte, redes e sites, tudo gerenciado por especialistas.")
    h = troca(h, "<!-- LADO DIREITO — 4 produtos principais + link -->", "<!-- LADO DIREITO — 5 frentes de serviço (cada uma leva à sua seção em Serviços) + link -->")
    cards = "".join([
        card_link("servicos.html#infraestrutura", "host", "Cloud privada",
                  "Arquivos, acessos, backup e segurança num ambiente só seu, cuidado pela gente."),
        card_link("servicos.html#sistemas", "automacao", "Sistemas e automação",
                  "CapyFiscal, Sistemas de Gestão e rotinas que hoje alguém faz na mão rodando sozinhas."),
        card_link("servicos.html#suporte", "suporte", "Suporte técnico",
                  "Chamado aberto, alguém que conhece o seu ambiente responde. Remoto ou na sua empresa."),
        card_link("servicos.html#redes", "cabo", "Rede do escritório",
                  "Pontos de rede, Wi-Fi e firewall para escritórios e lojas."),
        card_link("servicos.html#sites", "site", "Sites e hospedagem",
                  "Site novo, manutenção do site que você já tem e hospedagem de sistemas."),
    ])
    h, n = re.subn(r'<div class="space-y-5">.*?(\n          </div>\n\n          <div class="mt-8 reveal opacity-0">)',
                   lambda m: '<div class="fronts reveal opacity-0">' + cards + m.group(1), h, count=1, flags=re.S)
    assert n == 1

    # 4) Por que escolher: título e texto do original (com a grafia corrigida); quadradinhos da nova fase
    h = troca(h, 'Porque escolher a <span class="text-capy-gold">Capycloud</span> ?',
                 'Por que escolher a <span class="text-capy-gold">Capycloud</span>?')
    h = troca(h, "tranquilidade, seguranca e previsibilidade", "tranquilidade, segurança e previsibilidade")
    razoes = "".join([
        card_razao("alvo", "Você sabe quanto paga", "Cloud, CapyFiscal, hospedagem e manutenção têm mensalidade fixa. O que depende do caso, como suporte, rede e site, vem com orçamento antes de qualquer serviço."),
        card_razao("suporte", "Quem atende conhece o seu ambiente", "Sem fila de níveis de atendimento. Você fala com quem configurou a sua rede, o seu servidor ou o seu sistema."),
        card_razao("chave", "Seus dados continuam seus", "Ambiente dedicado, backup diário com cópia fora do escritório e nenhuma amarra: quando quiser, leva tudo embora."),
        card_razao("camadas", "Cresce no seu ritmo", "Contratou mais gente, abriu filial, precisou emitir nota? A estrutura acompanha sem comprar servidor novo nem contratar um técnico."),
        card_razao("rede", "Uma equipe para toda a TI", "Servidor, rede, computadores, site e nota fiscal com um contato só. Sem empurrar o problema de um fornecedor para o outro."),
        card_razao("usuarios", "Gente, não robô", "Usamos automação para não deixar nada passar, mas quem responde o seu chamado é uma pessoa, em português, em horário comercial."),
    ])
    h, n = re.subn(r'<!-- EFEITO 3: STAGGER nos cards -->\s*<div class="grid[^"]*">.*?(\n      </div>\n\n    </div>\n  </section>)',
                   lambda m: '<div class="fronts fronts-2 reveal opacity-0">' + razoes + m.group(1), h, count=1, flags=re.S)
    assert n == 1

    h = cta_sem_caixa(h, "Quer ver se faz sentido",
        r'<p class="text-capy-text text-lg mb-8 max-w-xl mx-auto text-justify">\s*Em uma conversa rápida.*?</p>',
        '<p class="text-capy-text text-lg mb-8 max-w-xl mx-auto">\n            Uma conversa rápida e a gente mostra o que dá para melhorar.\n          </p>')
    return h


def quemsomos():
    h = open(os.path.join(ORIG, "quemsomos.html"), encoding="utf-8").read()
    h = aplicar_casca(h, "quemsomos")
    h = cta_sem_caixa(h, "Quer conhecer a Capycloud",
        r'<p class="text-capy-text text-lg mb-8 max-w-xl mx-auto">\s*Em uma conversa rápida, entendemos.*?</p>',
        '<p class="text-capy-text text-lg mb-8 max-w-xl mx-auto">\n            Uma conversa rápida para entender a sua operação.\n          </p>')
    # Seção de software: título cita desenvolvimento e manutenção; texto justificado como o resto do site; sem travessão
    h = troca(h, 'Serviços de <span class="text-capy-gold">Software</span>',
                 'Desenvolvimento e <span class="text-capy-gold">Manutenção</span> de Software')
    h = troca(h, '<p class="text-capy-text text-base sm:text-lg leading-relaxed max-w-lg">',
                 '<p class="text-capy-text text-base sm:text-lg leading-relaxed max-w-lg text-justify">')
    h = troca(h, 'ajudar o seu negócio — ferramentas prontas para uso', 'ajudar o seu negócio: ferramentas prontas para uso')
    return h


def card_ancora(href, icone, titulo, texto):
    return f"""
          <a class="front" href="{href}">{ico(icone)}<div><strong>{titulo}</strong><small>{texto}</small></div></a>"""


TAGS = {"mes": ("svc-tag svc-tag-mes", "Mensalidade"), "analise": ("svc-tag svc-tag-analise", "Orçamento após análise"),
        "projeto": ("svc-tag svc-tag-projeto", "Por projeto")}


def svc_linha(icone, titulo, texto, tag):
    cls, rot = TAGS[tag]
    return f"""
          <div class="svc-row">
            <span class="svc-ico">{ico(icone)}</span>
            <div><h3>{titulo}</h3><p>{texto}</p></div>
            <span class="{cls}">{rot}</span>
          </div>"""


def svc_secao(ancora, fundo, titulo, texto, link, linhas):
    link_html = f'\n          <a class="svc-link" href="{link[0]}">{link[1]}</a>' if link else ""
    return f"""
  <section id="{ancora}" class="py-20 px-4 sm:px-6 lg:px-8 {fundo}">
    <div class="max-w-7xl mx-auto grid gap-10 lg:grid-cols-12">
      <div class="lg:col-span-4 lg:sticky lg:top-28 self-start reveal opacity-0">
        <h2 class="text-3xl sm:text-4xl font-extrabold text-capy-dark mb-4">{titulo}</h2>
        <p class="text-capy-text text-lg leading-relaxed">{texto}</p>{link_html}
      </div>
      <div class="lg:col-span-8 svc-ledger reveal opacity-0">{"".join(svc_linha(*l) for l in linhas)}
      </div>
    </div>
  </section>
"""


def secoes_servicos():
    """Descrição de cada frente, na ordem dos quadradinhos (a cloud já está nos 12 cards)."""
    return "".join([
        svc_secao("sistemas", "bg-capy-cream", 'Sistemas e <span class="text-capy-gold">automação</span>',
            "Software próprio e automações feitas para o jeito que a sua empresa trabalha.", None, [
            ("automacao", "Sistemas de Gestão", "Sistemas prontos para o seu ramo: estoque, vendas, contratos e nota fiscal pelo CapyFiscal, rodando na nossa infraestrutura.", "mes"),
            ("camadas", "Automações de rotina", "Cobranças, lembretes, relatórios diários no WhatsApp, planilhas que se preenchem sozinhas. O que hoje alguém faz na mão vira um fluxo automático.", "analise"),
            ("rede", "Integrações entre sistemas", "O sistema de vendas conversa com o financeiro, o site conversa com o estoque, a planilha conversa com o ERP. Sem redigitar nada.", "analise"),
            ("alvo", "Sistema sob medida", "Quando nada pronto resolve, a gente desenvolve. Começa pequeno, entra em uso cedo e cresce com o que o uso real mostrar.", "projeto"),
        ]),
        svc_secao("fiscal", "bg-white", '<span class="text-capy-gold">Capy</span>Fiscal',
            "Emissão de NF-e direto do seu sistema, sem redigitar nada em emissor gratuito. A partir de R$ 89 por mês.",
            ("capyfiscal.html", "Conhecer o CapyFiscal"), [
            ("nfe", "Emissão de NF-e por API", "O seu sistema manda os dados da venda, o CapyFiscal assina, envia para a SEFAZ e devolve o XML e o DANFE.", "mes"),
            ("pdf", "XML e DANFE por 5 anos", "Guarda legal dos arquivos, download a qualquer momento e pacote mensal pronto para o contador.", "mes"),
            ("painel", "Painel na Área do Cliente", "Notas, situação e rejeições explicadas, com o mesmo login da Área do Cliente da Capycloud.", "mes"),
        ]),
        svc_secao("suporte", "bg-capy-cream", 'Suporte <span class="text-capy-gold">técnico</span>',
            'Para quem não tem TI interna e cansou de chamar "o sobrinho". Chamado aberto, alguém que conhece o seu ambiente responde.',
            ("planos.html#manutencao", "Ver a manutenção remota mensal"), [
            ("remoto", "Manutenção remota mensal", "Uma mensalidade e a Capycloud vira a TI da sua empresa: computadores, rede, e-mail, impressora de rede e sistemas. Valor fechado depois de conhecer o seu ambiente.", "analise"),
            ("suporte", "Chamados avulsos", "Precisou de uma vez só? Abra o chamado, a gente avalia, passa o valor e resolve. Remoto ou presencial em Brasília e região.", "analise"),
            ("visita", "Visita técnica", "Instalação de equipamento, configuração de máquinas novas, diagnóstico no local. Valor combinado antes.", "analise"),
            ("manutencao", "Manutenção preventiva", "Atualizações, limpeza, ajustes e correções feitos com antecedência, antes de virarem incêndio.", "analise"),
        ]),
        svc_secao("redes", "bg-white", 'Rede do <span class="text-capy-gold">escritório</span>',
            "Para escritórios, lojas e consultórios. Internet que cai, Wi-Fi que não chega na sala dos fundos, cabo solto atrás do balcão: a gente organiza e deixa funcionando.",
            None, [
            ("cabo", "Pontos de rede", "Pontos novos, troca de cabos e identificação de cada ponto, em ambientes de pequeno porte.", "projeto"),
            ("host", "Organização do rack", "Switch, roteador e cabos arrumados e etiquetados. Quando der problema, todo mundo sabe onde mexer.", "projeto"),
            ("mapa", "Wi-Fi", "Sinal em todos os cômodos, rede separada para clientes e para a equipe.", "projeto"),
            ("manutencao", "Manutenção", "Diagnóstico e troca de equipamento. Sem contrato fixo quando é uma vez só.", "analise"),
        ]),
        svc_secao("sites", "bg-capy-cream", 'Sites e <span class="text-capy-gold">hospedagem</span>',
            "Site novo, site que já existe e precisa de quem cuide, ou um lugar seguro para rodar o sistema que você já usa.",
            ("planos.html#hospedagem", "Ver hospedagem e VPS"), [
            ("site", "Criação de sites", "Site institucional ou página de captação, rápido, no seu domínio, pronto para o Google. Conteúdo escrito junto com você.", "projeto"),
            ("manutencao", "Manutenção de site existente", "O site já existe, mas ninguém atualiza, o certificado venceu, a página caiu? Mensalidade com atualizações, backup e pequenas alterações incluídas.", "mes"),
            ("vps", "Hospedagem gerenciada e VPS", "Servidor virtual para o seu sistema, loja virtual ou aplicação de terceiros, com instalação, atualizações, backup e monitoramento por nossa conta.", "mes"),
            ("backup", "Armazenamento em nuvem", "Espaço extra para backup ou para compartilhar arquivos grandes, com criptografia, sem precisar do pacote completo.", "mes"),
        ]),
    ])


def servicos_orig():
    """Serviços volta ao ORIGINAL. Acréscimo: 6 quadradinhos com as frentes novas no espaço vazio
    que já existia antes dos 12 cards; os 12 cards ganham um título curto e a âncora #infraestrutura."""
    h = open(os.path.join(ORIG, "servicos.html"), encoding="utf-8").read()
    h = aplicar_casca(h, "servicos")
    h = troca(h, "Serviços Cloud - Capycloud</title>", "Serviços - Capycloud</title>")

    # Texto do hero: o original, com as frentes novas no mesmo ritmo
    h = troca(h,
        "Do armazenamento dos seus arquivos até a segurança da rede, cada serviço funciona junto com os outros, gerenciado pela nossa equipe.",
        "Dos seus arquivos à nota fiscal, da rede do escritório ao site da empresa: cada serviço funciona junto com os outros, gerenciado pela nossa equipe.")

    cards = "".join([
        card_ancora("#infraestrutura", "host", "Cloud privada",
                    "Arquivos, acessos, backup e segurança num ambiente só seu, cuidado pela gente."),
        card_ancora("#sistemas", "automacao", "Sistemas e automação",
                    "Sistemas de Gestão e rotinas que hoje alguém faz na mão rodando sozinhas."),
        card_ancora("#fiscal", "nfe", "CapyFiscal",
                    "Emissão de NF-e direto do seu sistema, a partir de R$ 89 por mês."),
        card_ancora("#suporte", "suporte", "Suporte técnico",
                    "Chamado aberto, alguém que conhece o seu ambiente responde. Remoto ou na sua empresa."),
        card_ancora("#redes", "cabo", "Rede do escritório",
                    "Pontos de rede, Wi-Fi e firewall para escritórios e lojas."),
        card_ancora("#sites", "site", "Sites e hospedagem",
                    "Site novo, manutenção do site que você já tem e hospedagem de sistemas."),
    ])
    h, n = re.subn(
        r'(<section class="py-20 px-4 sm:px-6 lg:px-8 bg-white">\s*<div class="max-w-7xl mx-auto">\s*)'
        r'<div class="text-center mb-12 reveal opacity-0">\s*<p class="text-capy-text text-lg max-w-2xl mx-auto text-justify">\s*</p>\s*</div>',
        lambda m: m.group(1).replace('<section class=', '<section id="infraestrutura" class=', 1)
        + '<div class="fronts fronts-3 reveal opacity-0 mb-20">' + cards + '\n        </div>\n\n'
        + '      <div class="text-center mb-12 reveal opacity-0">\n'
        + '        <h2 class="text-3xl sm:text-4xl font-extrabold text-capy-dark">O que vem na <span class="text-capy-gold">cloud privada</span></h2>\n'
        + '      </div>',
        h, count=1, flags=re.S)
    assert n == 1, "seção dos 12 cards não encontrada"

    BLOCO = r'  <!-- ═+\s*\n\s*'   # início do comentário que abre cada seção do original

    # "Como funciona na prática" e "Como cada serviço funciona" explicavam a cloud de novo (os 12 cards já fazem isso).
    # No lugar entram as outras frentes, na ordem dos quadradinhos.
    h, n = re.subn(BLOCO + r'SOLUÇÕES EM CAMADAS.*?(?=' + BLOCO + r'SEÇÃO 3: COMPARATIVO)',
                   lambda m: secoes_servicos() + "\n", h, count=1, flags=re.S)
    assert n == 1, "camadas/stack não encontradas"

    # Comparativo "TI Interno vs Capycloud" sai (pedido do Danylo em 23/10)
    h, n = re.subn(BLOCO + r'SEÇÃO 3: COMPARATIVO.*?(?=' + BLOCO + r'SEÇÃO 4)', '', h, count=1, flags=re.S)
    assert n == 1, "comparativo não encontrado"

    # "Precisa de algo específico?" repetia hospedagem/rede/armazenamento, que agora têm seção própria.
    cta = """  <!-- Fechamento, no mesmo estilo do fim da index -->
  <section class="py-20 px-4 sm:px-6 lg:px-8 bg-white">
    <div class="max-w-4xl mx-auto reveal opacity-0">
      <div class="text-center">
        <h2 class="text-3xl sm:text-4xl font-extrabold text-capy-dark mb-4">
          Não achou o que <span class="text-capy-gold">precisa</span>?
        </h2>
        <p class="text-capy-text text-lg mb-8 max-w-xl mx-auto">
          Conte o problema. Se não for com a gente, indicamos quem resolve.
        </p>
        <a href="faleconosco.html"
           class="inline-block px-10 py-4 bg-capy-gold hover:bg-capy-goldHover text-capy-dark font-bold rounded-xl transition-all shadow-lg hover:shadow-xl hover:-translate-y-1 text-lg fx-accent-pulse">
          Conversar com a equipe
        </a>
      </div>
    </div>
  </section>

"""
    h, n = re.subn(BLOCO + r'SEÇÃO 4: SERVIÇOS EXTRAS.*?(?=  <footer class="site-footer">)', lambda m: cta, h, count=1, flags=re.S)
    assert n == 1, "seção 4 não encontrada"
    return h


def main():
    saidas = {
        "index.html": index(),
        "quemsomos.html": quemsomos(),
        "servicos.html": servicos_orig(),
        "capyfiscal.html": pagina_nova(slug="capyfiscal.html", ativo="capyfiscal", title="CapyFiscal - Capycloud",
            desc="API de emissão de NF-e: o seu sistema manda a venda, a nota volta autorizada. A partir de R$ 89 por mês.", body=cp.capyfiscal(),
            extra_head='<link rel="stylesheet" href="css/capyfiscal-tema.css">'),
        "planos.html": pagina_nova(slug="planos.html", ativo="planos", title="Planos - Capycloud",
            desc="Cloud privada, CapyFiscal, hospedagem e VPS, sites e manutenção remota mensal.", body=cp.planos()),
        "faleconosco.html": pagina_nova(slug="faleconosco.html", ativo="faleconosco", title="Contato - Capycloud",
            desc="Fale com a Capycloud por WhatsApp, Telegram, e-mail ou formulário.", body=ot.faleconosco()),
        "area-do-cliente.html": pagina_nova(slug="area-do-cliente.html", ativo="area", title="Área do Cliente - Capycloud",
            desc="Área do Cliente da Capycloud.", body=ot.area_do_cliente(), noindex=True),
        "privacidade.html": pagina_nova(slug="privacidade.html", ativo="", title="Política de Privacidade - Capycloud",
            desc="Como a Capycloud trata os seus dados.", body=ot.privacidade()),
    }
    import pagina_api
    head_api, body_api = pagina_api.capyfiscal_api()
    saidas["capyfiscal-api.html"] = pagina_nova(slug="capyfiscal-api.html", ativo="capyfiscal", title="Documentação da API - CapyFiscal",
        desc="Referência completa da API do CapyFiscal.", body=body_api, extra_head=head_api)
    # OpenAPI público do CapyFiscal (sem rotas da fase 2, sem outros documentos, sem concorrente)
    import subprocess
    base = os.path.dirname(__file__)
    subprocess.run([sys.executable, os.path.join(base, "openapi_publica.py"), os.path.join(base, "esquemas-backend.json"),
                    os.path.join(OUT, "capyfiscal", "openapi.yaml")], check=True)
    for nome, html in saidas.items():
        open(os.path.join(OUT, nome), "w", encoding="utf-8").write(html)
        print("gerado", nome)


main()
