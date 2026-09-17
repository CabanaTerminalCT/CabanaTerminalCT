# =============================================================================
# 077 - Salva em JSON
# Nivel: 4 estrelas
# Conceitos: json.dump()
# =============================================================================
#
# HISTORIA
# --------
# JSON e o formato que a web fala. Salvar a ficha dos membros da CabanaTerminal
# em JSON permite ler de qualquer linguagem e mandar pra uma API depois.
#
# TAREFA
# ------
# 1. Crie um dicionario com dados de um membro (nome, nick, pontos)
# 2. Abra "membro.json" em modo escrita
# 3. Salve com json.dump(), com indentacao bonita
# 4. Leia de volta com json.load() e mostre
#
# Exemplo de execucao:
#
#   $ python3 077_salva_em_json.py
#   Salvo membro.json
#   Lido de volta: {'nome': 'Eduardo', 'nick': 'dudu', 'pontos': 42}
#
# REQUISITOS
# ----------
# [ ] Importa json
# [ ] Usa json.dump()
# [ ] Usa indent=2 (ou 4) pra formatar
# [ ] Le de volta com json.load()
#
# DICA
# ----
# json.dump(objeto, arquivo, indent=2, ensure_ascii=False) grava formatado e
# mantem acentos legiveis.
#
# VALIDACAO
# ---------
# O arquivo membro.json existe, formatado, e a leitura devolve o mesmo dict.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
