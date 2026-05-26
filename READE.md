# 🌿 Capycloud

**Cloud Privada Gerenciada** — Infraestrutura como Serviço (IaaS) construída 100% sobre tecnologias Open Source.

&gt; Sua empresa merece uma cloud que respeita seus dados, seu orçamento e sua soberania digital.

---

## 📦 Produtos

| Produto | Descrição | Stack |
|---------|-----------|-------|
| **CapyDrive** | Storage corporativo privado | TrueNAS, ZFS, NFS/SMB |
| **CapyAD** | Active Directory e SSO | Zentyal, LDAP, GPO |
| **CapyHost** | Hospedagem de SaaS, APIs e sites | Proxmox, Docker, Nginx |
| **CapyNet** | Firewall, VPN e segmentação de rede | OPNsense, WireGuard, VLANs |
| **CapyBackup** | Backup 3-2-1 automatizado | Borg, Rsync, replicação off-site |
| **CapyMonitor** | Monitoramento e dashboards | Zabbix, Grafana, SNMP |

---

## 🏗️ Arquitetura
Internet
↓
OPNsense (Firewall + VPN + VLANs)
↓
┌─────────┬─────────┬─────────┐
│ TrueNAS │ Zentyal │ Proxmox │
│ Storage │   AD    │ Compute │
└─────────┴─────────┴─────────┘
↓
Docker / VMs / Aplicações

---

## 🚀 Planos

| Recurso | Básico | Prata | Ouro |
|---------|--------|-------|------|
| CapyDrive | 500 GB | Expansível | Ilimitado* |
| CapyNet | VPN 5 users | + VLANs + Firewall IDS | + Site-to-site |
| CapyAD | — | ✅ | ✅ |
| CapyHost | — | 2 VMs/Containers | Ilimitado* |
| CapyBackup | Diário (7 dias) | Versionado (30 dias) | + Replicação DR |
| CapyMonitor | — | — | ✅ 24/7 |
| Suporte | Nível 1 | Nível 2 (SLA 1h) | Nível 3 (SLA 30min) |
| HA/Cluster | — | — | ✅ |

\* Dentro da capacidade do hardware dedicado contratado.

---

## 🛠️ Tecnologias

- **Storage:** TrueNAS (ZFS)
- **Virtualização:** Proxmox VE (KVM / LXC)
- **Firewall/VPN:** OPNsense (Suricata, WireGuard)
- **Identidade:** Zentyal (Samba AD, LDAP)
- **Monitoramento:** Zabbix + Grafana
- **Containers:** Docker + Docker Compose
- **Proxy:** Nginx
- **Backup:** BorgBackup + Rsync

---

## 📁 Estrutura do Projeto
Site-CapyCloud/
├── index.html              # Página inicial
├── servicos.html           # Catálogo de produtos
├── infraestrutura.html     # Stack tecnológica
├── planos.html             # Planos e preços
├── faleconosco.html        # Formulário de contato
├── css/
│   └── style.css           # Estilos customizados
├── js/
│   └── main.js             # Interatividade (menu, spotlight, scroll reveal)
└── img/                    # Imagens e assets


---

## 🎨 Design System

- **Framework CSS:** Tailwind CSS (CDN)
- **Paleta:** Slate 900 (fundo) + Emerald 400/500 (acento)
- **Fonte:** Sans-serif padrão do sistema
- **Efeitos:** Aurora animada, spotlight nos cards, grid tech, glow hover
- **Responsivo:** Mobile-first, menu hambúrguer em telas pequenas

---

## ⚡ Funcionalidades

- [x] Menu responsivo (desktop + mobile)
- [x] Efeito spotlight nos cards (mouse tracking)
- [x] Scroll reveal com IntersectionObserver
- [x] Link ativo destacado no menu
- [x] Formulário de contato integrado ao WhatsApp
- [x] Animações CSS (aurora, grid pulse, fade-in-up)

---

## 📞 Contato

- **WhatsApp:** [Conversar agora](https://wa.me/5562994879627)
- **Formulário:** `/faleconosco.html`
- **Resposta:** Em até 1 hora em horário comercial

---

## 📄 Licença

© 2025 Capycloud. Todos os direitos reservados.
