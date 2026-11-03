# Handoff: site da Capycloud e CapyFiscal (estado em 24/10/2026)

Este arquivo resume tudo o que foi feito na conversa anterior, para continuar num chat novo sem perder contexto.
No chat novo, anexe este arquivo e diga em qual frente quer trabalhar.

---

## 1. Como eu trabalho (para o assistente do próximo chat)

- Português do Brasil, direto, com um pouco de humor quando couber. Sem textos para agradar.
- Sou dev júnior: instruções técnicas passo a passo, sem resumir demais.
- Entregas: **um pacote único por rodada**, dizendo o que substitui, o que contém e **em qual pasta cada arquivo vai**.
- Nunca usar `~/Downloads`; os comandos partem da pasta do projeto. Nada de pastas de trabalho na raiz da home.
- Textos de tela e de site: **sem travessão**, português correto, nada de "IA explicando para iniciante".
- O cliente final não pode ver bastidor: nada de "Software Livre", nomes de concorrentes (Focus), estado específico (Goiás), detalhes de infraestrutura.
- Comandos destrutivos de banco (DROP, dropdb, pg_restore --clean, DELETE/UPDATE em massa, TRUNCATE): marcados como destrutivos, só como último recurso, sempre com backup antes e teste num banco temporário.
- Prefiro poucos documentos grandes a muitos pequenos.
- Mexer no visual do site: **mudanças cirúrgicas**. O visual original (menu, fonte do sistema, tamanho e posição das capivaras) é sagrado. Quando eu pedir para mexer em uma parte, mexer só nela.

---

## 2. Pastas no notebook

| Pasta | O que é |
|---|---|
| `~/Área de trabalho/Documentos/Site-CapyCloud/` | O site (HTML estático + Tailwind por CDN). Último pacote aplicado: **r26**. |
| `~/Área de trabalho/Documentos/Site-CapyCloud/capyfiscal/` | Deve conter **só** `openapi.yaml` (a documentação pública da API). |
| `~/Área de trabalho/Documentos/capyfiscal/` | Backend Flask do CapyFiscal (`capyfiscal/app`, `capyfiscal/tests`, `db/`, `docs/`). |
| `~/Área de trabalho/Documentos/entregas/` | Zips antigos. |

---

## 3. Site da Capycloud

### 3.1 Fonte da verdade

A partir de agora, **os arquivos HTML e CSS dentro de `Site-CapyCloud/` são a fonte da verdade**. Na conversa anterior eles eram gerados por scripts Python (pasta `gerador-site/` deste pacote). Esses scripts vão junto só como referência: se alguém rodar o gerador de novo, ele sobrescreve qualquer ajuste feito à mão nos HTML. Regra: ou edita os HTML direto (recomendado), ou volta a usar o gerador, nunca os dois misturados.

### 3.2 Regras de visual

- Fonte: a do sistema (o `body` usa `font-sans`). Não existe fonte Bulo no site.
- Cores: creme `#EDE4D7`, cobre `#B07340`, dourado `#C49A42`, texto `#4D4033`, títulos `#2D2926`, rodapé `#161410`.
- Menu (todas as páginas): Início, Quem Somos, Serviços, Planos, Contato, **CapyFiscal**, Área do Cliente.
- Topo de cada página: capivara à esquerda, texto à direita, no molde da página de Serviços original.
- Favicon novo: capivara de óculos com fundo transparente (`favicon.ico` na raiz, `img/favicon-32.png`, `img/favicon-192.png`, `img/apple-touch-icon.png`, original em `img/capy-transparente.png`).

### 3.3 CSS

| Arquivo | Para quê |
|---|---|
| `css/style.css` | O original (432 linhas) mais blocos acrescentados no fim: raios do topo, rodapé novo, ícones, quadradinhos (`.fronts`), listas de Serviços (`.svc-*`). |
| `css/paginas-novas.css` | Componentes das páginas novas (planos, tabelas, botões). No fim: alinhamento de Planos (rodada 9), grade de 5 planos, títulos centralizados em Planos. |
| `css/capyfiscal-tema.css` | Só na página do CapyFiscal: faixas alternando entre o tom do rodapé e o creme, ícones de traço fino. |
| `css/capyfiscal-api.css` | Só na documentação da API: mesmo esquema de cores e o Swagger com as cores da marca. |

### 3.4 Estado das páginas

| Página | Estado |
|---|---|
| `index.html` | Pronta. Ecossistema com imagem nova (`img/capyservindex.png`, texto do card trocado para "Sistemas de Gestão"), quadradinhos com links, "Por que escolher" com quadradinhos. |
| `quemsomos.html` | Pronta. Original com ajustes de texto no bloco de software. |
| `servicos.html` | Pronta. Original + 6 quadradinhos + seções por frente (Sistemas, CapyFiscal, Suporte, Rede, Sites). Sem "TI Interno x Capycloud". |
| `planos.html` | Pronta. CapyLight R$ 899 (até 2 usuários, valores provisórios), cloud, CapyFiscal, hospedagem e VPS, sites (landing a partir de R$ 299, institucional sob orçamento, manutenção R$ 149), manutenção remota em tabela. Imagem do topo provisória (`capidev_fundobranco.webp`). |
| `capyfiscal.html` | Pronta. Imagem nova (`img/capyfiscal.webp`, recortada de fundo preto). Sequência: topo e Como funciona escuros; Para quem é e O que vem incluído creme; Planos escuro; Desenvolvedores creme; Perguntas escuro; chamada final creme. |
| `capyfiscal-api.html` | Pronta na rodada 26 (capivara do CapyFiscal no topo). Guia (endereços, autenticação, caminho de uma nota, situações, erros, avisos) + referência das rotas (Swagger). |
| `faleconosco.html`, `area-do-cliente.html`, `privacidade.html` | **Ainda não passaram pelo pente fino.** |

### 3.5 Pendências do site

1. Pente fino em Contato e Área do Cliente.
2. Arte da capivara do CapyFiscal no padrão do site, **já com fundo branco ou transparente**; depois, trocar `img/capyfiscal.webp` mantendo o nome.
3. Arte própria para o topo de Planos (hoje usa a capivara dev).
4. Decidir preços do CapyFiscal. Comparação feita com a Focus (Solo R$ 94,90 / Start R$ 119,90 / Growth R$ 572): sugestão foi **Rede de R$ 149 para R$ 109** e **nota adicional do plano Loja de R$ 0,15 para R$ 0,10**. Não aplicado.
5. CapyElite e CapyEnterprise dizem "até 30 usuários" (veio do site original); definir o número do Enterprise.
6. Limpeza de imagens sem uso (cerca de 22 MB de PNG e variações de fonte) e reduzir o `capyaba.png` (1 MB).
7. VPS: preços conferidos e mantidos (R$ 149 / 249 / 449, gerenciados). Opcional: VPS 1 com 8 GB em vez de 4 GB.

---

## 4. CapyFiscal (backend Flask)

### 4.1 Estado

- Esqueleto completo em Flask + Postgres 16: API `/v2` (NF-e, inutilização, webhooks, empresas, arquivos, status), fila no Postgres, worker, webhooks assinados (HMAC), certificado cifrado (AES-256-GCM, chave mestra fora do banco), painel com SSO da Área do Cliente.
- Motor de emissão: **só o motor falso** (homologação). O motor real com a PyNFe é a próxima grande etapa.
- Testes: 5 passando (`pytest -q` com `TEST_DATABASE_URL` apontando para um banco cujo nome contém "test").
- Documento principal: `docs/CAPYFISCAL-ENGENHARIA-REVERSA.md` (seções 0 a 13). A seção 13 explica o pente fino de 24/10.

### 4.2 Pente fino de 24/10 (já aplicado no pacote `capyfiscal-r2-pente-fino.zip`)

- `/v2/status` público sem detalhes internos; `sefaz_go` virou `sefaz`.
- E-mail da nota e prévia de DANFE respondem 501 até existirem de verdade.
- CFOP começando com 4 passou a ser recusado.
- Webhook aceita só o evento `nfe` (a inutilização ainda não dispara aviso).
- Documentação pública reescrita a partir do código (campos tirados dos modelos Pydantic).

### 4.3 Próximos passos (nesta ordem)

1. Motor real com a PyNFe (`app/motor/pynfe_motor.py`): montar o XML, validar no XSD, assinar, transmitir, consultar, gerar DANFE.
2. SMTP para enviar XML e DANFE por e-mail (aí a rota de e-mail volta a funcionar).
3. Painel: upload do certificado por link, tokens, inutilizações pendentes, detalhe da nota.
4. Integração no MotoGestor (provedor HTTP compatível).
5. Deploy na VM (Gunicorn + worker no systemd, Cloudflare Tunnel, chave mestra em `/etc/capyfiscal/`).

Falta saber: subdomínios confirmados, URL da Área do Cliente, versão do Python da VM, um certificado A1 de homologação.

### 4.4 Sobre trocar para Node ou Java

Decisão: **seguir em Python/Flask**. Motivos registrados:
- Numa API de nota fiscal, o tempo de cada nota é dominado pela SEFAZ (segundos), não pela linguagem. O gargalo nunca vai ser o Flask.
- O que faz uma API dessas ser boa já está no projeto: fila, idempotência pela referência, retentativas, webhooks assinados, validação antes da SEFAZ, testes.
- Reescrever jogaria fora código testado e o aprendizado de Flask, que é um dos objetivos.
- Ponto honesto: Java tem o ecossistema de NF-e mais maduro. Se a PyNFe travar em algo, o motor é isolado (`app/motor/`), então dá para ligar um serviço pequeno em outra linguagem só para assinar e transmitir, sem reescrever a API.

---

## 5. Guia de Git para o repositório da organização no GitHub

Cada passo diz o que o comando faz. Rode na pasta do projeto.

### 5.1 Uma vez só, na máquina

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email-do-github@exemplo.com"
gh auth login          # escolha GitHub.com, HTTPS, e entre pelo navegador
```

Para baixar o projeto (fica numa pasta nova dentro de Documentos):

```bash
cd ~/"Área de trabalho/Documentos"
git clone https://github.com/NOME-DA-ORGANIZACAO/NOME-DO-REPO.git
cd NOME-DO-REPO
```

### 5.2 O ciclo de toda tarefa

1. **Atualize a `main` antes de começar**
   ```bash
   git switch main
   git pull
   ```
2. **Crie um galho (branch) para a tarefa**: nome curto, com o tipo na frente.
   ```bash
   git switch -c feat/tela-de-login        # feat = coisa nova; fix = correção; docs = documentação
   ```
3. **Trabalhe e veja o que mudou**
   ```bash
   git status            # lista arquivos alterados
   git diff              # mostra as linhas alteradas
   ```
4. **Salve um ponto (commit)**: escolha os arquivos e escreva o que fez.
   ```bash
   git add caminho/do/arquivo.py           # ou: git add -p  (vai perguntando pedaço por pedaço)
   git commit -m "Tela de login com validação de e-mail"
   ```
   Faça commits pequenos, um por ideia. Nunca adicione `.env`, senhas ou certificados.
5. **Mande o galho para o GitHub**
   ```bash
   git push -u origin feat/tela-de-login   # o -u só na primeira vez; depois, só git push
   ```
6. **Abra o Pull Request (PR)**: é o pedido para juntar o seu galho na `main`.
   ```bash
   gh pr create --fill                     # ou pelo botão "Compare & pull request" no site
   ```
   O outro programador revisa, comenta, você ajusta com novos commits e `git push`.
7. **Merge**: quando aprovado, clique em "Squash and merge" no GitHub (junta tudo num commit só na `main`).
8. **Volte para a `main` e limpe**
   ```bash
   git switch main
   git pull
   git branch -d feat/tela-de-login
   ```

### 5.3 Quando a `main` andou enquanto você trabalhava

```bash
git switch feat/tela-de-login
git fetch
git merge origin/main
```

Se aparecer **conflito**, o Git marca no arquivo:

```
<<<<<<< HEAD
a sua versão
=======
a versão que veio da main
>>>>>>> origin/main
```

Apague as marcas, deixe o código como deve ficar, e então:

```bash
git add arquivo-resolvido.py
git commit                      # o Git já sugere a mensagem do merge
git push
```

Se ficar perdido no meio do conflito: `git merge --abort` volta tudo como estava antes do merge.

### 5.4 Socorro

| Situação | Comando |
|---|---|
| Ver o histórico | `git log --oneline --graph -20` |
| Guardar mudanças para trocar de galho | `git stash` (depois `git stash pop`) |
| Desfazer o último commit que **ainda não** foi enviado, mantendo as mudanças | `git reset --soft HEAD~1` |
| **Destrutivo**: jogar fora as mudanças de um arquivo que não foram commitadas | `git restore caminho/do/arquivo` |
| Saber em qual galho estou | `git branch --show-current` |

Regras de ouro: nunca trabalhar direto na `main`; nunca usar `git push --force` em galho que outra pessoa usa; perguntar ao outro programador se a `main` é protegida (exige PR) e qual o padrão de nome de galho e de mensagem de commit do time.

---

## 6. Conteúdo deste pacote

| Item | Para quê |
|---|---|
| `HANDOFF-CAPYCLOUD.md` | Este arquivo. |
| `gerador-site/` | Scripts Python que geraram o site e a documentação da API (referência; ver seção 3.1). `openapi_publica.py` + `esquemas-backend.json` geram o `capyfiscal/openapi.yaml`. |
| `site-original/` | Os HTML originais do site, antes de qualquer mudança (o gerador parte deles). |
