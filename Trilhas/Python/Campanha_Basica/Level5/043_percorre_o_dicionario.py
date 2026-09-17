# =============================================================================
# 043 - Percorre o dicionario
# Nivel: 3 estrelas
# Conceitos: .keys(), .values(), .items()
# =============================================================================
#
# HISTORIA
# --------
# Pra imprimir o placar da CabanaTerminal formatado, voce precisa percorrer as
# chaves e os valores do dicionario. .items() e a ferramenta principal pra
# isso.
#
# TAREFA
# ------
# 1. Crie um dict de membro -> pontos
# 2. Imprima so as chaves
# 3. Imprima so os valores
# 4. Imprima cada par no formato "membro: pontos"
#
# Exemplo de execucao:
#
#   $ python3 043_percorre_o_dicionario.py
#   Chaves: ['ana', 'bruno', 'carla']
#   Valores: [10, 20, 15]
#   --- placar ---
#   ana: 10
#   bruno: 20
#   carla: 15
#
# REQUISITOS
# ----------
# [ ] Usa .keys()
# [ ] Usa .values()
# [ ] Usa .items() com for
#
# DICA
# ----
# .items() devolve pares (chave, valor), que voce desempacota no for:
#
#   for nome, pontos in placar.items():
#       print(f"{nome}: {pontos}")
#
# VALIDACAO
# ---------
# O placar lista os 3 membros na ordem de insercao com seus pontos.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
