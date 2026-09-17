# =============================================================================
# 018 - Pula o 7
# Nivel: 3 estrelas
# Conceitos: continue
# =============================================================================
#
# HISTORIA
# --------
# Supersticao na CabanaTerminal: ninguem fala o numero 7 durante a contagem
# do mutirao. Voce vai contar de 1 a 20, mas sempre que o numero for multiplo
# de 7, o loop pula com continue e nem imprime.
#
# TAREFA
# ------
# 1. Conte de 1 a 20
# 2. Nao imprima os multiplos de 7 (7 e 14)
# 3. Imprima os demais numeros
#
# Exemplo de execucao:
#
#   $ python3 018_pula_o_7.py
#   1
#   2
#   ...
#   6
#   8
#   ...
#   13
#   15
#   ...
#   20
#
# REQUISITOS
# ----------
# [ ] Usa for com range(1, 21)
# [ ] Usa continue pra pular os multiplos de 7
# [ ] Detecta multiplo com o operador %
#
# DICA
# ----
# Um numero e multiplo de 7 quando "n % 7 == 0":
#
#   for n in range(1, 21):
#       if n % 7 == 0:
#           continue
#       print(n)
#
# Diferenca: break SAI do loop, continue PULA so a volta atual.
#
# VALIDACAO
# ---------
# A saida tem 18 numeros. O 7 e o 14 nao aparecem.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
