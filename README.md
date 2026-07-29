# Capycloud — Site Corporativo

**Cloud Privada Gerenciada** — Infraestrutura como Serviço (IaaS) construída 100% sobre tecnologias Open Source.

> Sua empresa merece uma cloud que responde, respeita seus dados, seu orçamento e sua soberania digital.

---

## Produtos Capycloud

| Produto | O que sua empresa recebe | Stack |
|---------|--------------------------|-------|
| **CapyDrive** | Servidor de arquivos centralizado — todos os documentos em um lugar seguro, acessível de qualquer dispositivo | TrueNAS, ZFS, Snapshots |
| **CapyAD** | Gestão de usuários e permissões — controle de quem acessa o quê, SSO e conformidade LGPD | Zentyal, LDAP, GPO, SSO |
| **CapyHost** | Hospedagem de sistemas, APIs e sites — VMs e containers dedicados, deploy gerenciado | Proxmox, Docker, Nginx |
| **CapyNet** | Acesso remoto seguro + Firewall — VPN criptografada, IDS/IPS, segmentação por VLANs | OPNsense, WireGuard, Suricata |
| **CapyBackup** | Backup automatizado — política 3-2-1, versionado e replicado off-site, recuperação em minutos | Borg, Rsync, Replicação off-site |
| **CapyMonitor** | Monitoramento 24/7 — dashboards em tempo real, alertas preventivos | Zabbix, Grafana, SNMP |

---

## Planos

| Recurso | CapyEssential | CapyPro | CapyElite | CapyEnterprise |
|---------|---------------|---------|-----------|----------------|
| **Usuários** | Até 5 | Até 15 | Até 30 | Até 30 |
| **Storage** | 200 GB | 500 GB | 1 TB | 1 TB |
| **Chamados/mês** | 5 | 15 | 30 | Ilimitado (uso justo) |
| **SLA Resposta** | 8h úteis | 4h úteis | 1h útil | 1h útil + emergencial |
| **Preço** | Sob Consulta | Sob Consulta | Sob Consulta | Sob Consulta |
| **Destaque** | Essencial para equipes small | Mais escolhido | Controle avançado + auditoria | Prioridade máxima + suporte ilimitado |

> Armazenamento e usuários adicionais sob demanda. Serviços limitados ao ambiente gerenciado Capycloud.

---

## Comparativo de Custos — TI Interno vs Capycloud

| Item | TI Interno | Capycloud |
|------|------------|-----------|
| Custo mensal | R$ 12k – 20k+ | Sob Consulta |
| Investimento inicial | Alto (~R$ 36k) | Nenhum |
| Equipe técnica | Necessária (salários + encargos ~70%) | Inclusa |
| Manutenção | Interna | Inclusa |
| Escalabilidade | Limitada (re-investir hardware) | Alta (sem custo extra de infra) |
| Risco operacional | Alto (ferias, rotatividade, erros) | Controlado (SLA garantido) |
| **Projeção 5 anos** | **R$ 748k – 1.245M** | **Economia de R$ 448k – 1.185M** |

---

## Arquitetura

```
Internet
  ↓
OPNsense (Firewall + VPN + VLANs + IDS/IPS)
  ↓
┌─────────┬─────────┬─────────┐
│ TrueNAS │ Zentyal │ Proxmox │
│ Storage │   AD    │ Compute │
└─────────┴─────────┴─────────┘
  ↓
Docker / VMs / Aplicações
  ↓
Zabbix + Grafana (Monitoramento 24/7)
  ↓
Borg + Rsync (Backup 3-2-1 → Off-site DR)
```

---

## Tecnologias

- **Storage:** TrueNAS (ZFS, snapshots, deduplicação, replicação)
- **Virtualização:** Proxmox VE (KVM / LXC)
- **Firewall/VPN:** OPNsense (Suricata IDS/IPS, WireGuard, VLANs)
- **Identidade:** Zentyal (Samba AD, LDAP, GPO, SSO)
- **Monitoramento:** Zabbix + Grafana (24/7, dashboards, alertas)
- **Containers:** Docker + Docker Compose
- **Proxy:** Nginx (SSL automático, balanceamento)
- **Backup:** BorgBackup + Rsync (3-2-1, deduplicação, off-site)

---

## Estrutura do Projeto

```
Site-CapyCloud/
├── index.html              # Home — hero, produtos, comparativo custos, 10 vantagens, projeção 5 anos, CTA
├── servicos.html           # "O que você recebe" (negócio), stack por dentro (tech), comparativo custos, projeção 5 anos
├── infraestrutura.html     # Stack tecnológica detalhada
├── planos.html             # 4 tiers (CapyEssential/Pro/Elite/Enterprise), Sob Consulta, SLA detalhado
├── faleconosco.html        # Formulário contato + WhatsApp + SLA garantido + sidebar detalhes
├── README.md               # Esta documentação
├── css/
│   └── style.css           # Animações e efeitos custom (aurora, spotlight, glow, reveal, shimmer)
├── js/
│   └── main.js             # Menu mobile, spotlight, scroll reveal, WhatsApp form redirect, nav-link active
└── img/                    # Imagens e assets (vazio por enquanto)
```

---

## Conteúdo por Página

### index.html
- **Hero:** Aurora + glow + grid tech effects, badge "Cloud Privada Gerenciada", stats (100% Open Source, Zero Vendor Lock-in, Dedicado)
- **Produtos Capy:** 6 cards (CapyDrive/AD/Host/Net/Backup/Monitor) com tags de stack
- **Comparativo de Custos:** TI Interno vs Capycloud — breakdown detalhado + tabela resumo + projeção 5 anos
- **10 Vantagens:** Redução custos, Ambiente seguro, Acesso remoto VPN, Gestão usuários, Alta disponibilidade, Escalabilidade, Suporte especializado, Previsibilidade custo, Proteção dados, Foco negócio
- **CTA Final:** "Pronto para sair das Big Techs?"

### servicos.html
- **Hero:** "O que sua empresa recebe" — perspectiva negócio
- **Seção 1 — O que você recebe:** 9 cards em linguagem de negócio (Servidor Arquivos, VPN, Gestão Usuários, Backup, Monitoramento 24/7, Hospedagem Sistemas, Firewall/Segurança, Suporte SLA, Auditoria/Relatórios)
- **Seção 2 — A Stack por dentro:** 6 blocos alternados com detalhes técnicos de cada CapyProduct
- **Seção 3 — Comparativo:** TI Interno vs Capycloud simplificado + projeção 5 anos (R$ 748k–1.245M vs Economia R$ 448k–1.185M)
- **CTA Final:** "Pronto para focar no negócio?"

### planos.html
- **Hero:** "Planos de Cloud Privada"
- **Grid 4 tiers:** CapyEssential (5 users, 200GB, 5 tickets, SLA 8h), CapyPro (15 users, 500GB, 15 tickets, SLA 4h — "Mais Escolhido"), CapyElite (30 users, 1TB, 30 tickets, SLA 1h), CapyEnterprise (30 users, 1TB, ∞ tickets, SLA 1h + emergencial)
- **SLA Garantido:** 4 cards com tempo de resposta e chamados incluídos por plano
- **Plano Customizado:** CapyMail, CapyDB, CapyVoIP etc.

### faleconosco.html
- **Hero:** "Fale com um Especialista"
- **Formulário:** Nome, e-mail, empresa, telefone, mensagem → redirect WhatsApp
- **Sidebar:** Card WhatsApp direto, SLA Garantido (tabela por plano), Observações importantes

---

## Design System

- **Framework CSS:** Tailwind CSS (CDN) — layout, componentes, responsivo
- **CSS Customizado:** Apenas animações e efeitos que Tailwind não cobre
  - Aurora background, Aurora glow, Grid pulse
  - Text shimmer, Fade in up, Badge pulse
  - Spotlight card (mouse-tracking glow), Glow card (hover border + shadow)
  - Scroll reveal (IntersectionObserver), Custom scrollbar
- **Paleta:** Slate 900 (fundo principal) + Emerald 400/500 (acento/destaque) + Red 400 (alerta/custo TI Interno)
- **Fonte:** Inter (Google Fonts) — 400/500/600/700/800/900
- **Responsivo:** Mobile-first, menu hamburger em telas < md, grid adapta de 1→2→3→4 colunas

---

## Funcionalidades JS

- [x] Menu responsivo — hamburger → X toggle com SVG swap, close on link click
- [x] Spotlight card — mouse tracking com CSS custom properties (--mouse-x, --mouse-y)
- [x] Scroll reveal — IntersectionObserver (threshold 0.1), add .revealed + .animate-fade-in-up
- [x] Formulário contato → WhatsApp redirect (55 62 9948-79627)
- [x] Nav-link active — match current page filename, add .active class

---

## Estratégia de Preços

- **Website:** Todos os planos mostram "Sob Consulta" — sem preço fixo publicado
- **Proposta direta:** Valores reais apresentados em conversa/proposta individual
- **Argumento:** Mensalidade Capycloud (~R$ 1k–5k) vs TI Interno (~R$ 12k–20k) = economia R$ 448k–1.185M em 5 anos

---

## Contato

- **WhatsApp:** [Conversar agora](https://wa.me/5562994879627)
- **Formulário:** `/faleconosco.html`
- **SLA Resposta:** CapyEnterprise até 1h útil + emergencial | CapyElite 1h | CapyPro 4h | CapyEssential 8h

---

## Licença

© 2026 Capycloud. Todos os direitos reservados.

