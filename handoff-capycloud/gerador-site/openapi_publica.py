"""Gera o OpenAPI PÚBLICO do CapyFiscal (capyfiscal/openapi.yaml do site).

Escrito do zero a partir do que o backend Flask (capyfiscal-r1) faz de verdade:
- rotas, códigos HTTP e corpos de resposta conferidos em app/api/*.py;
- campos de NF-e e de empresa tirados dos modelos Pydantic (esquemas-backend.json, exportado do backend),
  com as descrições em português escritas aqui.
Rotas que o backend ainda não entrega de verdade (envio por e-mail e prévia de DANFE) ficam de fora.

Uso: python3 openapi_publica.py <esquemas-backend.json> <saida.yaml>
"""
import json
import re
import sys

import yaml

ESQ = json.load(open(sys.argv[1], encoding="utf-8"))
SAIDA = sys.argv[2]


def R(nome):
    return {"$ref": f"#/components/schemas/{nome}"}


# ───────────────────────────── conversão dos modelos Pydantic (JSON Schema 2020) para OpenAPI 3.0
def _tipo(p):
    """Simplifica anyOf de Pydantic: Decimal vira number, Optional vira nullable."""
    if "anyOf" in p:
        tipos = [x for x in p["anyOf"] if x.get("type") != "null"]
        nulo = len(tipos) < len(p["anyOf"])
        if any(x.get("type") == "number" for x in tipos):
            base = {"type": "number"}
        else:
            base = dict(tipos[0])
        if nulo:
            base["nullable"] = True
        return base
    base = {k: v for k, v in p.items() if k in ("type", "items", "$ref")}
    return base


def converter(modelo, descricoes, exemplo=None, ocultar=()):
    props = {}
    for nome, p in modelo["properties"].items():
        if nome in ocultar:
            continue
        q = _tipo(p)
        if "items" in q and "$ref" in q["items"]:
            q["items"] = R(q["items"]["$ref"].split("/")[-1])
        for k in ("maxLength", "minLength", "maximum", "minimum"):
            if k in p:
                q[k] = p[k]
        if "anyOf" in p:
            for x in p["anyOf"]:
                for k in ("maxLength", "minLength"):
                    if k in x:
                        q[k] = x[k]
        if "default" in p and p["default"] is not None:
            d = p["default"]
            if q.get("type") == "number" and isinstance(d, str):
                d = float(d) if "." in d else int(d)
            q["default"] = d
        if nome not in descricoes:
            raise SystemExit(f"falta descrição para o campo {nome}")
        q["description"] = descricoes[nome]
        props[nome] = q
    sch = {"type": "object", "properties": props}
    req = [r for r in modelo.get("required", []) if r not in ocultar]
    if req:
        sch["required"] = req
    if exemplo:
        sch["example"] = exemplo
    return sch


# ───────────────────────────── descrições dos campos
D_NFE = {
    "natureza_operacao": "Natureza da operação, como aparece na nota. Ex.: Venda de mercadoria.",
    "data_emissao": "Data e hora da emissão em ISO 8601, com fuso horário. Ex.: 2026-11-03T10:15:00-03:00.",
    "tipo_documento": "0 = entrada, 1 = saída.",
    "local_destino": "1 = operação interna, 2 = interestadual, 3 = com o exterior.",
    "finalidade_emissao": "1 = normal, 2 = complementar, 3 = ajuste, 4 = devolução.",
    "consumidor_final": "0 = normal, 1 = consumidor final.",
    "presenca_comprador": "0 = não se aplica, 1 = presencial, 2 = pela internet, 3 = por telefone, "
                          "5 = presencial fora do estabelecimento, 9 = outros.",
    "cnpj_emitente": "Opcional. Se informado, precisa ser o CNPJ da empresa dona do token. "
                     "Os demais dados do emitente vêm do cadastro da empresa.",
    "cpf_destinatario": "CPF do destinatário. Informe CPF ou CNPJ, nunca os dois.",
    "cnpj_destinatario": "CNPJ do destinatário. Informe CPF ou CNPJ, nunca os dois.",
    "nome_destinatario": "Nome ou razão social do destinatário.",
    "indicador_inscricao_estadual_destinatario": "1 = contribuinte do ICMS, 2 = contribuinte isento, 9 = não contribuinte. "
                                                 "Para CPF é sempre 9 e é preenchido automaticamente.",
    "inscricao_estadual_destinatario": "Inscrição estadual do destinatário, quando houver.",
    "logradouro_destinatario": "Logradouro do destinatário.",
    "numero_destinatario": "Número do endereço. Aceita texto, como SN.",
    "bairro_destinatario": "Bairro do destinatário.",
    "codigo_municipio_destinatario": "Código IBGE do município, com 7 dígitos. Precisa ser da mesma UF de uf_destinatario.",
    "municipio_destinatario": "Nome do município do destinatário.",
    "uf_destinatario": "Sigla da UF do destinatário.",
    "cep_destinatario": "CEP do destinatário, com 8 dígitos.",
    "email_destinatario": "E-mail do destinatário, gravado na nota.",
    "modalidade_frete": "0 = por conta do emitente, 1 = do destinatário, 2 = de terceiros, 3 = transporte próprio do remetente, "
                        "4 = transporte próprio do destinatário, 9 = sem frete.",
    "valor_frete": "Valor total do frete.",
    "valor_seguro": "Valor total do seguro.",
    "valor_desconto": "Valor total do desconto.",
    "valor_outras_despesas": "Valor das outras despesas acessórias.",
    "valor_produtos": "Soma do valor_bruto dos itens que entram no total. Se não for enviado, é calculado; se for, precisa bater.",
    "valor_total": "Produtos − desconto + frete + seguro + outras despesas. Se não for enviado, é calculado; se for, precisa bater.",
    "itens": "Itens da nota, pelo menos um, com numero_item em sequência a partir de 1. O nome items também é aceito.",
    "formas_pagamento": "Obrigatório em nota de saída. A soma dos valores precisa ser igual a valor_total "
                        "(exceto quando a forma é 90, sem pagamento).",
    "informacoes_adicionais_contribuinte": "Informações complementares, impressas no DANFE.",
}
D_ITEM = {
    "numero_item": "Número do item, de 1 a 990, em sequência.",
    "codigo_produto": "Código do produto no seu sistema.",
    "descricao": "Descrição do produto.",
    "codigo_ncm": "NCM com 8 dígitos.",
    "cfop": "CFOP com 4 dígitos. O primeiro dígito precisa combinar com a operação: saída interna 5, interestadual 6, "
            "exterior 7; entrada interna 1, interestadual 2, exterior 3.",
    "unidade_comercial": "Unidade de venda, como UN, KG ou CX.",
    "quantidade_comercial": "Quantidade, maior que zero.",
    "valor_unitario_comercial": "Valor unitário, maior que zero.",
    "valor_bruto": "Quantidade × valor unitário. Se não for enviado, é calculado; se for, precisa bater.",
    "inclui_no_total": "1 = soma no total da nota, 0 = não soma.",
    "icms_origem": "Origem da mercadoria, de 0 a 8 (0 = nacional).",
    "icms_situacao_tributaria": "CST do ICMS (2 dígitos, regime normal) ou CSOSN (3 dígitos, Simples Nacional).",
    "icms_modalidade_base_calculo": "Modalidade da base de cálculo do ICMS. Na CST 20, se não for enviada, usa 3 (valor da operação).",
    "icms_reducao_base_calculo": "Percentual de redução da base de cálculo. Obrigatório na CST 20.",
    "icms_base_calculo": "Base de cálculo do ICMS. Na CST 20, é calculada se não for enviada.",
    "icms_aliquota": "Alíquota do ICMS, em %. Obrigatória na CST 20.",
    "icms_valor": "Valor do ICMS. Na CST 20, é calculado se não for enviado.",
    "pis_situacao_tributaria": "CST do PIS.",
    "cofins_situacao_tributaria": "CST da COFINS.",
    "codigo_beneficio_fiscal": "Código de benefício fiscal (cBenef), quando a UF exigir. Vale só para CST 20, 30, 40, 41, 50, 51, 70 e 90.",
    "ibs_cbs_situacao_tributaria": "CST do IBS e da CBS, quando aplicável.",
    "ibs_cbs_classificacao_tributaria": "Classificação tributária do IBS e da CBS (cClassTrib), quando aplicável.",
}
D_PAG = {
    "forma_pagamento": "Código da forma de pagamento: 01 dinheiro, 02 cheque, 03 cartão de crédito, 04 cartão de débito, "
                       "15 boleto, 17 PIX, 90 sem pagamento, 99 outros.",
    "valor_pagamento": "Valor pago nesta forma.",
    "indicador_pagamento": "0 = à vista, 1 = a prazo.",
    "descricao_pagamento": "Descrição da forma de pagamento. Obrigatória quando forma_pagamento é 99.",
}
D_EMP = {
    "nome": "Razão social.",
    "nome_fantasia": "Nome fantasia.",
    "cnpj": "CNPJ da empresa.",
    "inscricao_estadual": "Inscrição estadual.",
    "inscricao_municipal": "Inscrição municipal.",
    "regime_tributario": "1 = Simples Nacional, 2 = Simples Nacional com excesso de sublimite, 3 = regime normal, 4 = MEI.",
    "logradouro": "Logradouro.",
    "numero": "Número do endereço. Aceita texto, como SN.",
    "complemento": "Complemento do endereço.",
    "bairro": "Bairro.",
    "codigo_municipio": "Código IBGE do município, com 7 dígitos.",
    "municipio": "Nome do município.",
    "uf": "Sigla da UF.",
    "cep": "CEP, com 8 dígitos.",
    "telefone": "Telefone.",
    "email": "E-mail de contato.",
    "cpf_cnpj_contabilidade": "CPF ou CNPJ da contabilidade. Algumas UFs exigem na nota.",
    "habilita_nfe": "Habilita a emissão de NF-e.",
    "discrimina_impostos": "Calcula e imprime o valor aproximado dos tributos (Lei da Transparência).",
    "orientacao_danfe": "Layout do DANFE: portrait (retrato), landscape (paisagem) ou simplified (simplificado).",
    "recibo_danfe": "Imprime o canhoto de recebimento no DANFE.",
    "serie_nfe_producao": "Série da NF-e em produção.",
    "proximo_numero_nfe_producao": "Próximo número da NF-e em produção. Use para continuar a numeração de outro emissor.",
    "serie_nfe_homologacao": "Série da NF-e no ambiente de testes.",
    "proximo_numero_nfe_homologacao": "Próximo número da NF-e no ambiente de testes.",
    "arquivo_certificado_base64": "Certificado digital A1 (arquivo .pfx ou .p12) em base64.",
    "senha_certificado": "Senha do certificado. Obrigatória quando arquivo_certificado_base64 é enviado.",
    "certificado_especifico": "Marca o certificado como exclusivo desta empresa.",
}
# aceitos pelo backend, mas ainda sem efeito: ficam fora da documentação
EMP_OCULTOS = ("enviar_email_destinatario", "enviar_email_homologacao", "nfe_sincrono", "nfe_sincrono_homologacao")

EX_ITEM = {"numero_item": 1, "codigo_produto": "CAM-001", "descricao": "Camiseta algodão M", "codigo_ncm": "61091000",
           "cfop": "5102", "unidade_comercial": "UN", "quantidade_comercial": 2, "valor_unitario_comercial": 49.9,
           "icms_origem": 0, "icms_situacao_tributaria": "102", "pis_situacao_tributaria": "07", "cofins_situacao_tributaria": "07"}
EX_NFE = {"natureza_operacao": "Venda de mercadoria", "data_emissao": "2026-11-03T10:15:00-03:00",
          "tipo_documento": 1, "local_destino": 1, "cpf_destinatario": "12345678909", "nome_destinatario": "Maria da Silva",
          "logradouro_destinatario": "Rua das Flores", "numero_destinatario": "120", "bairro_destinatario": "Centro",
          "codigo_municipio_destinatario": "3550308", "municipio_destinatario": "São Paulo", "uf_destinatario": "SP",
          "cep_destinatario": "01001000", "itens": [EX_ITEM], "formas_pagamento": [{"forma_pagamento": "17", "valor_pagamento": 99.8}]}
EX_EMP = {"nome": "Loja Exemplo Ltda", "nome_fantasia": "Loja Exemplo", "cnpj": "11222333000181", "inscricao_estadual": "123456789",
          "regime_tributario": 1, "logradouro": "Avenida Central", "numero": "1000", "bairro": "Centro",
          "codigo_municipio": "3550308", "municipio": "São Paulo", "uf": "SP", "cep": "01001000",
          "arquivo_certificado_base64": "MIIK...", "senha_certificado": "senha-do-certificado"}

nfe_m = ESQ["NFeRequest"]
schemas = {
    "NFe": converter(nfe_m, D_NFE, EX_NFE, ocultar=("items",)),
    "Item": converter(nfe_m["$defs"]["Item"], D_ITEM),
    "FormaPagamento": converter(nfe_m["$defs"]["FormaPagamento"], D_PAG),
    "EmpresaNova": converter(ESQ["EmpresaCreate"], D_EMP, EX_EMP, ocultar=EMP_OCULTOS),
    "EmpresaAlteracao": converter(ESQ["EmpresaUpdate"], D_EMP, {"telefone": "1133334444", "proximo_numero_nfe_producao": 1532},
                                  ocultar=EMP_OCULTOS),
}
schemas["NFe"]["title"] = "Nota fiscal (envio)"
schemas["EmpresaAlteracao"].pop("required", None)
schemas["EmpresaAlteracao"]["description"] = "Envie só os campos que vão mudar."

ST = {"type": "string"}
schemas.update({
    "Erro": {"type": "object", "properties": {
        "codigo": {"type": "string", "description": "Código do erro, estável para o seu sistema tratar."},
        "mensagem": {"type": "string", "description": "Explicação em português."},
        "erros": {"type": "array", "items": R("ErroCampo"), "description": "Presente nos erros de validação: um item por campo."}}},
    "ErroCampo": {"type": "object", "properties": {
        "campo": {"type": "string", "description": "Campo com problema. Itens aparecem como itens[2].cfop."},
        "mensagem": {"type": "string"}}},
    "Nota": {"type": "object", "description": "Situação da nota. Os campos presentes dependem do status.", "properties": {
        "cnpj_emitente": ST, "ref": {"type": "string", "description": "A referência que o seu sistema enviou."},
        "status": {"type": "string", "enum": ["processando_autorizacao", "autorizado", "erro_autorizacao", "cancelado", "denegado"]},
        "status_sefaz": {"type": "string", "description": "Código de retorno da SEFAZ (cStat)."},
        "mensagem_sefaz": {"type": "string", "description": "Mensagem da SEFAZ."},
        "chave_nfe": {"type": "string", "description": "Chave de acesso, com o prefixo NFe."},
        "numero": ST, "serie": ST, "protocolo": {"type": "string", "description": "Número do protocolo de autorização."},
        "caminho_xml_nota_fiscal": {"type": "string", "description": "Caminho para baixar o XML autorizado."},
        "caminho_danfe": {"type": "string", "description": "Caminho para baixar o DANFE em PDF."},
        "caminho_xml_cancelamento": {"type": "string", "description": "Só em notas canceladas."},
        "numero_carta_correcao": {"type": "integer", "description": "Sequência da última carta de correção autorizada."},
        "caminho_xml_carta_correcao": ST, "caminho_pdf_carta_correcao": {"type": "string", "nullable": True},
        "erros": {"type": "array", "items": {"type": "object"}, "description": "Só em erro_autorizacao: detalhes da rejeição."},
        "requisicao_nota_fiscal": {"type": "object", "description": "Só com completa=1: os dados enviados, já normalizados."},
        "protocolo_nota_fiscal": {"type": "object", "description": "Só com completa=1: dados do protocolo da SEFAZ."}}},
    "Cancelamento": {"type": "object", "required": ["justificativa"], "properties": {
        "justificativa": {"type": "string", "minLength": 15, "maxLength": 255, "description": "Motivo do cancelamento."}},
        "example": {"justificativa": "Venda desfeita a pedido do cliente"}},
    "CancelamentoResultado": {"type": "object", "properties": {
        "status": {"type": "string", "enum": ["cancelado", "erro_cancelamento"]},
        "status_sefaz": ST, "mensagem_sefaz": ST,
        "caminho_xml_cancelamento": {"type": "string", "description": "Presente quando o cancelamento é autorizado."}}},
    "CartaCorrecao": {"type": "object", "required": ["correcao"], "properties": {
        "correcao": {"type": "string", "minLength": 15, "maxLength": 1000, "description": "Texto da correção."}},
        "example": {"correcao": "O endereço correto do destinatário é Rua das Flores, 210."}},
    "CartaCorrecaoResultado": {"type": "object", "properties": {
        "status": {"type": "string", "enum": ["autorizado", "erro_autorizacao"]}, "status_sefaz": ST, "mensagem_sefaz": ST,
        "numero_carta_correcao": {"type": "integer"}, "caminho_xml_carta_correcao": ST,
        "caminho_pdf_carta_correcao": {"type": "string", "nullable": True}}},
    "Inutilizacao": {"type": "object", "required": ["cnpj", "serie", "numero_inicial", "numero_final", "justificativa"], "properties": {
        "cnpj": {"type": "string", "description": "CNPJ da empresa. Com token de empresa, precisa ser o da própria empresa."},
        "serie": {"type": "integer"}, "numero_inicial": {"type": "integer"}, "numero_final": {"type": "integer"},
        "justificativa": {"type": "string", "minLength": 15, "maxLength": 255}},
        "example": {"cnpj": "11222333000181", "serie": 1, "numero_inicial": 120, "numero_final": 122,
                    "justificativa": "Falha no sistema pulou a numeração"}},
    "InutilizacaoResultado": {"type": "object", "properties": {
        "status": {"type": "string", "enum": ["autorizado", "erro_autorizacao"]}, "status_sefaz": ST, "mensagem_sefaz": ST,
        "cnpj": ST, "modelo": ST, "serie": ST, "numero_inicial": ST, "numero_final": ST,
        "protocolo_sefaz": ST, "caminho_xml": ST, "data_recebimento": {"type": "string", "nullable": True}}},
    "Gatilho": {"type": "object", "properties": {
        "id": ST, "url": ST, "event": {"type": "string", "enum": ["nfe"]}, "cnpj": ST,
        "authorization": {"type": "string", "nullable": True}, "authorization_header": {"type": "string", "nullable": True}}},
    "GatilhoNovo": {"allOf": [R("Gatilho"), {"type": "object", "properties": {"segredo_hmac": {
        "type": "string", "description": "Chave para conferir a assinatura de cada aviso. Aparece só nesta resposta: guarde."}}}]},
    "GatilhoCadastro": {"type": "object", "required": ["event", "url"], "properties": {
        "event": {"type": "string", "enum": ["nfe"], "description": "nfe: a nota foi autorizada, recusada, denegada ou cancelada."},
        "url": {"type": "string", "description": "Endereço do seu sistema que vai receber os avisos (http ou https)."},
        "cnpj": {"type": "string", "description": "Obrigatório com token de integrador. Com token de empresa, é a própria empresa."},
        "authorization": {"type": "string", "description": "Valor enviado num cabeçalho de autenticação, se o seu sistema exigir."},
        "authorization_header": {"type": "string", "description": "Nome desse cabeçalho. Ex.: Authorization."}},
        "example": {"event": "nfe", "url": "https://meusistema.com.br/avisos/nfe"}},
    "Empresa": {"type": "object", "properties": {
        "id": {"type": "integer"}, **{k: v for k, v in schemas["EmpresaNova"]["properties"].items()
                                      if k not in ("arquivo_certificado_base64", "senha_certificado")},
        "certificado_valido_de": {"type": "string", "nullable": True}, "certificado_valido_ate": {"type": "string", "nullable": True},
        "certificado_cnpj": {"type": "string", "nullable": True}, "data_ultima_emissao": {"type": "string", "nullable": True},
        "ativo": {"type": "boolean"}}},
    "EmpresaCriada": {"allOf": [R("Empresa"), {"type": "object", "properties": {
        "token_producao": {"type": "string", "description": "Token da empresa para produção. Aparece só nesta resposta."},
        "token_homologacao": {"type": "string", "description": "Token da empresa para o ambiente de testes. Aparece só nesta resposta."}}}]},
    "Simulacao": {"type": "object", "properties": {"dry_run": {"type": "boolean"}, "mensagem": ST}},
    "Status": {"type": "object", "properties": {
        "api": {"type": "string", "enum": ["ok", "erro"]},
        "ambiente": {"type": "integer", "description": "1 = produção, 2 = testes."},
        "sefaz": {"type": "object", "nullable": True, "properties": {
            "cStat": {"type": "string", "description": "107 = em operação; 108 ou 109 = paralisada."},
            "xMotivo": ST, "consultado_em": ST}}},
        "example": {"api": "ok", "ambiente": 1, "sefaz": {"cStat": "107", "xMotivo": "Servico em Operacao",
                                                          "consultado_em": "2026-11-03T10:30:00-03:00"}}},
})


# ───────────────────────────── respostas
def resp(desc, schema=None, exemplo=None, tipo="application/json"):
    r = {"description": desc}
    if schema is not None:
        c = {"schema": schema}
        if exemplo is not None:
            c["example"] = exemplo
        r["content"] = {tipo: c}
    return r


def erro(desc, codigo, mensagem, status=None):
    return resp(desc, R("Erro"), {"codigo": codigo, "mensagem": mensagem})


E401 = {"$ref": "#/components/responses/NaoAutorizado"}
E404 = {"$ref": "#/components/responses/NaoEncontrado"}
E415 = {"$ref": "#/components/responses/SemCorpo"}
E429 = {"$ref": "#/components/responses/LimiteExcedido"}
responses = {
    "NaoAutorizado": erro("Token ausente, inválido ou de outro ambiente.", "nao_autorizado", "Token inválido ou ausente."),
    "NaoEncontrado": erro("Não encontrado.", "nao_encontrado", "Nota fiscal não encontrada."),
    "SemCorpo": erro("A requisição chegou sem corpo JSON.", "formato_invalido", "Recebida requisição vazia quando eram esperados dados."),
    "LimiteExcedido": erro("Limite de requisições por minuto excedido.", "limite_excedido",
                           "Limite de 100 requisições por minuto excedido para este token."),
}

NOTA_AUT = {"cnpj_emitente": "11222333000181", "ref": "venda-123", "status": "autorizado", "status_sefaz": "100",
            "mensagem_sefaz": "Autorizado o uso da NF-e", "chave_nfe": "NFe35261111222333000181550010000015321000015320",
            "numero": "1532", "serie": "1", "protocolo": "135260000123456",
            "caminho_xml_nota_fiscal": "/arquivos/11222333000181/202611/XMLs/35261111222333000181550010000015321000015320-nfe.xml",
            "caminho_danfe": "/arquivos/11222333000181/202611/DANFEs/35261111222333000181550010000015321000015320.pdf"}
NOTA_ERRO = {"cnpj_emitente": "11222333000181", "ref": "venda-123", "status": "erro_autorizacao", "status_sefaz": "598",
             "mensagem_sefaz": "Rejeição: total da NF difere do somatório dos valores",
             "erros": [{"mensagem": "Total da NF difere do somatório dos valores que compõem o total da NF"}]}

REF = {"name": "referencia", "in": "path", "required": True, "schema": {"type": "string", "pattern": "^[A-Za-z0-9_-]{1,64}$"},
       "description": "A referência que o seu sistema deu à nota no envio."}

paths = {}


def op(caminho, metodo, tag, resumo, descricao, respostas, corpo=None, params=None, seguranca=True, servidores=None):
    o = {"tags": [tag], "summary": resumo, "description": descricao, "responses": respostas}
    if corpo:
        o["requestBody"] = {"required": True, "content": {"application/json": {"schema": corpo}}}
    if params:
        o["parameters"] = params
    if not seguranca:
        o["security"] = []
    if servidores:
        o["servers"] = servidores
    paths.setdefault(caminho, {})[metodo] = o


T_NFE, T_NUM, T_ARQ, T_HOOK, T_EMP, T_SRV = "Notas fiscais", "Numeração", "Arquivos", "Avisos (webhooks)", "Empresas", "Serviço"

op("/nfe", "post", T_NFE, "Emitir uma nota",
   "Recebe os dados da nota, confere e coloca na fila de envio à SEFAZ. A resposta vem na hora com "
   "`processando_autorizacao`; o resultado chega pelo aviso (webhook) ou pela consulta.\n\n"
   "**Reenvio com a mesma referência:** se a nota ainda está em processamento, volta `pending_operation`; se já foi "
   "autorizada, cancelada ou denegada, volta `already_processed`; se foi rejeitada (`erro_autorizacao`), os novos dados "
   "são aceitos como uma nova tentativa da mesma nota.",
   {"202": resp("Recebida e na fila.", R("Nota"), {"cnpj_emitente": "11222333000181", "ref": "venda-123", "status": "processando_autorizacao"}),
    "400": erro("Referência ausente ou inválida.", "requisicao_invalida", 'Parâmetro "ref" inválido: use letras, números, "-" e "_" (até 64 caracteres).'),
    "401": E401, "415": E415,
    "422": resp("Dados inválidos ou nota já em andamento.", R("Erro"), {"codigo": "erro_validacao_schema", "mensagem": "Erro na validação dos dados da nota.",
                "erros": [{"campo": "itens[1].cfop", "mensagem": "CFOP 6102 incompatível: saída com local_destino 1 pede CFOP iniciado em 5"}]}),
    "429": E429},
   corpo=R("NFe"),
   params=[{"name": "ref", "in": "query", "required": True, "schema": {"type": "string", "pattern": "^[A-Za-z0-9_-]{1,64}$"},
            "description": "Referência única da nota no seu sistema (letras, números, - e _, até 64 caracteres). "
                           "É por ela que você consulta, cancela e corrige a nota depois."}])

op("/nfe/{referencia}", "get", T_NFE, "Consultar uma nota",
   "Devolve a situação atual da nota. Depois da autorização, traz a chave, o número, o protocolo e os caminhos do XML e do DANFE.",
   {"200": resp("Situação da nota.", R("Nota"), NOTA_AUT), "401": E401, "404": E404, "429": E429},
   params=[REF, {"name": "completa", "in": "query", "required": False, "schema": {"type": "integer", "enum": [0, 1]},
                 "description": "1 = inclui os dados enviados e o protocolo completo da SEFAZ."}])

op("/nfe/{referencia}", "delete", T_NFE, "Cancelar uma nota",
   "Cancela uma nota autorizada. A resposta já traz o resultado da SEFAZ. O prazo legal para cancelar é de 24 horas "
   "depois da autorização na maioria das UFs.",
   {"200": resp("Resultado do cancelamento.", R("CancelamentoResultado"),
                {"status": "cancelado", "status_sefaz": "135", "mensagem_sefaz": "Evento registrado e vinculado a NF-e",
                 "caminho_xml_cancelamento": "/arquivos/11222333000181/202611/XMLs/35261111222333000181550010000015321000015320-can.xml"}),
    "400": erro("Justificativa fora do tamanho ou nota não autorizada.", "requisicao_invalida", 'Parâmetro "justificativa" deve ter entre 15 e 255 caracteres.'),
    "401": E401, "404": E404, "415": E415,
    "422": erro("A nota já foi cancelada.", "already_processed", "A nota fiscal já foi cancelada."), "429": E429},
   corpo=R("Cancelamento"), params=[REF])

op("/nfe/{referencia}/carta_correcao", "post", T_NFE, "Emitir carta de correção",
   "Corrige informações de uma nota autorizada. A resposta já traz o resultado da SEFAZ. Cada nota aceita até 20 cartas; "
   "a mais recente substitui as anteriores.\n\nA carta de correção não pode alterar valores, impostos, dados cadastrais "
   "que mudem o emitente ou o destinatário, nem a data de emissão ou de saída.",
   {"200": resp("Resultado da carta de correção.", R("CartaCorrecaoResultado")),
    "400": erro("Texto fora do tamanho ou nota não autorizada.", "nfe_nao_autorizada", "Nota fiscal não autorizada."),
    "401": E401, "404": E404, "415": E415,
    "422": erro("Limite de cartas atingido.", "limite_cartas", "Limite de 20 cartas de correção atingido para esta nota."), "429": E429},
   corpo=R("CartaCorrecao"), params=[REF])

op("/nfe/inutilizacao", "post", T_NUM, "Inutilizar numeração",
   "Informa à SEFAZ que uma faixa de números não será usada. No dia a dia não é preciso: o CapyFiscal controla a "
   "numeração e não pula números. Use quando a numeração de outro emissor deixou um buraco.",
   {"200": resp("Resultado da inutilização.", R("InutilizacaoResultado")),
    "400": erro("Parâmetros ausentes ou inválidos.", "requisicao_invalida", 'Parâmetros obrigatórios: justificativa.'),
    "401": E401, "415": E415, "429": E429},
   corpo=R("Inutilizacao"))

op("/nfe/inutilizacoes", "get", T_NUM, "Listar inutilizações",
   "Lista as faixas inutilizadas de uma empresa, das mais recentes para as mais antigas.",
   {"200": resp("Lista de inutilizações.", {"type": "array", "items": R("InutilizacaoResultado")}),
    "400": erro("CNPJ não informado.", "requisicao_invalida", 'Parâmetros "cnpj" ou "cpf" não informados.'), "401": E401, "429": E429},
   params=[{"name": "cnpj", "in": "query", "required": True, "schema": ST, "description": "CNPJ da empresa."},
           {"name": "data_recebimento_inicial", "in": "query", "schema": {"type": "string", "format": "date"}},
           {"name": "data_recebimento_final", "in": "query", "schema": {"type": "string", "format": "date"}},
           {"name": "numero_inicial", "in": "query", "schema": {"type": "integer"}},
           {"name": "numero_final", "in": "query", "schema": {"type": "integer"}}])

op("/nfe/{referencia}/hook", "post", T_HOOK, "Reenviar o aviso de uma nota",
   "Manda de novo o aviso da situação atual da nota para todos os endereços cadastrados. Útil para testes ou para "
   "recuperar um aviso que o seu sistema perdeu.",
   {"200": resp("Avisos agendados.", {"type": "array", "items": {"type": "object", "properties": {"id": ST, "event": ST}}}),
    "401": E401, "404": E404, "429": E429}, params=[REF])

for ext, tipo, resumo in ((".xml", "application/xml", "Baixar o XML autorizado"), (".pdf", "application/pdf", "Baixar o DANFE em PDF")):
    op(f"/nfe/{{referencia}}{ext}", "get", T_ARQ, resumo,
       "Atalho pela referência. O mesmo arquivo pode ser baixado pelo caminho devolvido na consulta.",
       {"200": resp("Arquivo.", {"type": "string", "format": "binary"}, tipo=tipo),
        "401": E401, "404": E404, "422": erro("A nota ainda não foi autorizada.", "nfe_nao_autorizada", "Nota ainda não autorizada."), "429": E429},
       params=[REF])

op("/arquivos/{cnpj}/{periodo}/{pasta}/{arquivo}", "get", T_ARQ, "Baixar um arquivo pelo caminho",
   "Os campos `caminho_...` das respostas apontam para esta rota. Ela fica no endereço do servidor, sem o `/v2`, "
   "e exige o token da empresa dona do arquivo (ou o de integrador).",
   {"200": resp("Arquivo (XML ou PDF).", {"type": "string", "format": "binary"}, tipo="application/octet-stream"),
    "401": E401, "404": erro("Arquivo não encontrado.", "nao_encontrado", "Arquivo não encontrado."), "429": E429},
   params=[{"name": "cnpj", "in": "path", "required": True, "schema": ST},
           {"name": "periodo", "in": "path", "required": True, "schema": ST, "description": "Ano e mês da emissão (AAAAMM)."},
           {"name": "pasta", "in": "path", "required": True, "schema": {"type": "string", "enum": ["XMLs", "DANFEs"]}},
           {"name": "arquivo", "in": "path", "required": True, "schema": ST}],
   servidores=[{"url": "https://api-fiscal.capycloud.com.br", "description": "Produção"},
               {"url": "https://homologacao-fiscal.capycloud.com.br", "description": "Testes"}])

op("/hooks", "post", T_HOOK, "Cadastrar um endereço de aviso",
   "Cadastra o endereço do seu sistema que vai receber os avisos. Guarde o `segredo_hmac` da resposta: ele não aparece de novo.",
   {"200": resp("Gatilho criado.", R("GatilhoNovo")),
    "400": erro("Evento ou URL inválidos.", "requisicao_invalida", 'Parâmetro "url" deve começar com http:// ou https://.'),
    "401": E401, "415": E415, "429": E429},
   corpo=R("GatilhoCadastro"))
op("/hooks", "get", T_HOOK, "Listar endereços de aviso", "Lista os gatilhos ativos visíveis para o token.",
   {"200": resp("Lista.", {"type": "array", "items": R("Gatilho")}), "401": E401, "429": E429})
op("/hooks/{id}", "get", T_HOOK, "Consultar um endereço de aviso", "Devolve um gatilho pelo id.",
   {"200": resp("Gatilho.", R("Gatilho")), "401": E401,
    "404": erro("Gatilho não encontrado.", "nao_encontrado", "Gatilho não encontrado"), "429": E429},
   params=[{"name": "id", "in": "path", "required": True, "schema": ST}])
op("/hooks/{id}", "delete", T_HOOK, "Excluir um endereço de aviso", "Para de enviar avisos para este endereço.",
   {"200": resp("Gatilho excluído.", R("Gatilho")), "401": E401,
    "404": erro("Gatilho não encontrado.", "nao_encontrado", "Gatilho não encontrado"), "429": E429},
   params=[{"name": "id", "in": "path", "required": True, "schema": ST}])

DRY = {"name": "dry_run", "in": "query", "required": False, "schema": {"type": "integer", "enum": [0, 1]},
       "description": "1 = só confere os dados, sem gravar nada."}
EID = {"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}
E422_EMP = resp("Dados inválidos.", R("Erro"), {"codigo": "erro_validacao", "mensagem": "Erro de validação",
                                                  "erros": [{"campo": "codigo_municipio", "mensagem": "código IBGE do município deve ter 7 dígitos"}]})
op("/empresas", "post", T_EMP, "Cadastrar uma empresa",
   "Cadastra uma empresa emissora e já devolve os dois tokens dela, de produção e de testes. Os tokens aparecem só "
   "nesta resposta. Exige o token de integrador.",
   {"200": resp("Empresa cadastrada (ou simulação, com dry_run=1).", {"oneOf": [R("EmpresaCriada"), R("Simulacao")]}),
    "401": E401, "415": E415, "422": E422_EMP, "429": E429},
   corpo=R("EmpresaNova"), params=[DRY])
op("/empresas", "get", T_EMP, "Listar empresas", "Lista as empresas do integrador, 50 por página.",
   {"200": resp("Lista.", {"type": "array", "items": R("Empresa")}), "401": E401, "429": E429},
   params=[{"name": "cnpj", "in": "query", "schema": ST, "description": "Filtra por CNPJ."},
           {"name": "offset", "in": "query", "schema": {"type": "integer", "default": 0}, "description": "Quantos registros pular."}])
op("/empresas/{id}", "get", T_EMP, "Consultar uma empresa", "Devolve os dados de uma empresa.",
   {"200": resp("Empresa.", R("Empresa")), "401": E401,
    "404": erro("Empresa não encontrada.", "nao_encontrado", "Empresa não encontrada."), "429": E429}, params=[EID])
op("/empresas/{id}", "put", T_EMP, "Alterar uma empresa",
   "Altera os campos enviados. Para trocar o certificado, envie `arquivo_certificado_base64` e `senha_certificado`.",
   {"200": resp("Empresa alterada (ou simulação, com dry_run=1).", {"oneOf": [R("Empresa"), R("Simulacao")]}),
    "401": E401, "404": erro("Empresa não encontrada.", "nao_encontrado", "Empresa não encontrada."), "415": E415,
    "422": E422_EMP, "429": E429}, corpo=R("EmpresaAlteracao"), params=[EID, DRY])
op("/empresas/{id}", "delete", T_EMP, "Desativar uma empresa",
   "Desativa a empresa e revoga os tokens dela. As notas já emitidas continuam guardadas pelo prazo legal.",
   {"200": resp("Empresa desativada.", R("Empresa")), "401": E401,
    "404": erro("Empresa não encontrada.", "nao_encontrado", "Empresa não encontrada."), "429": E429}, params=[EID])

op("/status", "get", T_SRV, "Situação do serviço",
   "Mostra se a API está no ar e a última situação conhecida da SEFAZ. Não exige token.",
   {"200": resp("Situação.", R("Status"))}, seguranca=False)

spec = {
    "openapi": "3.0.3",
    "info": {"title": "CapyFiscal API", "version": "1.0",
             "description": "API de emissão de NF-e (modelo 55, layout 4.00) da Capycloud."},
    "servers": [{"url": "https://api-fiscal.capycloud.com.br/v2", "description": "Produção"},
                {"url": "https://homologacao-fiscal.capycloud.com.br/v2", "description": "Testes (homologação)"}],
    "security": [{"BasicAuth": []}, {"BearerAuth": []}],
    "tags": [
        {"name": T_NFE, "description": "Emitir, consultar, cancelar e corrigir notas. Usa o token da empresa."},
        {"name": T_NUM, "description": "Inutilização de números que não serão usados."},
        {"name": T_ARQ, "description": "Download do XML e do DANFE."},
        {"name": T_HOOK, "description": "Avisos automáticos para o seu sistema quando a nota muda de situação."},
        {"name": T_EMP, "description": "Cadastro das empresas emissoras. Usa o token de integrador."},
        {"name": T_SRV, "description": "Situação do serviço."},
    ],
    "paths": paths,
    "components": {
        "securitySchemes": {
            "BasicAuth": {"type": "http", "scheme": "basic", "description": "Usuário = token, senha em branco."},
            "BearerAuth": {"type": "http", "scheme": "bearer", "description": "Authorization: Bearer TOKEN"}},
        "schemas": schemas, "responses": responses},
}

saida = yaml.safe_dump(spec, allow_unicode=True, sort_keys=False, width=120)
proibido = re.findall(r"(?i)focus|goi[aá]s|SEFAZ-GO|\bfase\b|x-capyfiscal|worker|nfce|nfse|mdfe|\bct-?e\b|tpAmb|—", saida)
assert not proibido, sorted(set(proibido))
open(SAIDA, "w", encoding="utf-8").write(saida)
print("rotas públicas:", sum(len(v) for v in paths.values()), "| schemas:", len(schemas))
