# =============================================================================
# 034 - Ordena a bagunca
# Nivel: 3 estrelas
# Conceitos: .sort(), sorted(), .reverse()
# =============================================================================
#
# HISTORIA
# --------
# Os pontos do mutirao da CabanaTerminal chegaram fora de ordem. Pra montar o
# ranking, voce precisa ordenar do maior pro menor (ou o contrario).
#
# TAREFA
# ------
# 1. Crie uma lista de numeros desordenada
# 2. Ordene em ordem crescente com sorted() e mostre (sem alterar a original)
# 3. Ordene a original em ordem decrescente com .sort(reverse=True)
# 4. Inverta a lista com .reverse()
#
# Exemplo de execucao:
#
#   $ python3 034_ordena_a_bagunca.py
#   Original: [5, 2, 9, 1, 7]
#   Crescente (sorted): [1, 2, 5, 7, 9]
#   Original intacta: [5, 2, 9, 1, 7]
#   Decrescente (sort): [9, 7, 5, 2, 1]
#
# REQUISITOS
# ----------
# [ ] Usa sorted()
# [ ] Usa .sort(reverse=True)
# [ ] Usa .reverse()
#
# DICA
# ----
# Diferenca importante:
#   sorted(lista)  -> devolve uma nova lista ordenada, nao muda a original
#   lista.sort()   -> ordena a propria lista, no lugar (retorna None)
#
# VALIDACAO
# ---------
# [5,2,9,1,7] -> crescente [1,2,5,7,9] e decrescente [9,7,5,2,1].
# =============================================================================


# >>> SEU CODIGO AQUI <<<
