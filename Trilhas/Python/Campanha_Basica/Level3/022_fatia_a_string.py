# =============================================================================
# 022 - Fatia a string
# Nivel: 2 estrelas
# Conceitos: slicing [a:b]
# =============================================================================
#
# HISTORIA
# --------
# As vezes a gente so quer um pedaco do texto - um prefixo, um sufixo, o meio.
# O slicing da CabanaTerminal e a tesoura que corta strings sem estragar o
# original.
#
# TAREFA
# ------
# 1. Peca uma palavra ao usuario
# 2. Mostre os 3 primeiros caracteres
# 3. Mostre os 3 ultimos caracteres
# 4. Mostre a palavra invertida (usando slice)
#
# Exemplo de execucao:
#
#   $ python3 022_fatia_a_string.py
#   Palavra: cabana
#   Primeiros 3: cab
#   Ultimos 3: ana
#   Invertida: anabac
#
# REQUISITOS
# ----------
# [ ] Usa slice [0:3] (ou [:3])
# [ ] Usa slice negativo pros ultimos [-3:]
# [ ] Inverte com [::-1]
#
# DICA
# ----
# O fim do slice fica de fora: "cabana"[0:3] -> "cab". Passo negativo
# inverte: "cabana"[::-1] -> "anabac".
#
# VALIDACAO
# ---------
# "cabana" -> "cab", "ana", "anabac".
# =============================================================================


# >>> SEU CODIGO AQUI <<<
