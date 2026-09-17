# =============================================================================
# 032 - Fatia a lista
# Nivel: 2 estrelas
# Conceitos: slicing de lista
# =============================================================================
#
# HISTORIA
# --------
# Voce tem o ranking inteiro da CabanaTerminal, mas so quer o podio (top 3) e
# os lanterninhas (ultimos). O slicing funciona em listas igual funciona em
# strings.
#
# TAREFA
# ------
# 1. Crie uma lista de pelo menos 6 numeros
# 2. Mostre os 3 primeiros
# 3. Mostre os 3 ultimos
# 4. Mostre a lista invertida
#
# Exemplo de execucao:
#
#   $ python3 032_fatia_a_lista.py
#   Lista: [10, 20, 30, 40, 50, 60]
#   Primeiros 3: [10, 20, 30]
#   Ultimos 3: [40, 50, 60]
#   Invertida: [60, 50, 40, 30, 20, 10]
#
# REQUISITOS
# ----------
# [ ] Usa slice [:3]
# [ ] Usa slice [-3:]
# [ ] Inverte com [::-1]
#
# DICA
# ----
# Slicing de lista devolve uma NOVA lista. O fim fica de fora: [0:3] pega os
# indices 0, 1 e 2.
#
# VALIDACAO
# ---------
# [10,20,30,40,50,60] -> [10,20,30], [40,50,60], [60,...,10].
# =============================================================================


# >>> SEU CODIGO AQUI <<<
