# =============================================================================
# 012 - Contagem regressiva
# Nivel: 2 estrelas
# Conceitos: while, -= (decremento)
# =============================================================================
#
# HISTORIA
# --------
# Toda boa sessao de CTF da CabanaTerminal comeca com contagem regressiva.
# Bum, bum, bum... e "foguete!" pro desafio comecar. Voce vai automatizar
# esse ritual no terminal.
#
# TAREFA
# ------
# 1. Comece em 10
# 2. Imprima os numeros de 10 ate 0, um por linha
# 3. Ao chegar em 0, imprima "foguete!"
#
# Exemplo de execucao:
#
#   $ python3 012_contagem_regressiva.py
#   10
#   9
#   ...
#   1
#   0
#   foguete!
#
# REQUISITOS
# ----------
# [ ] Usa while
# [ ] Usa -= pra diminuir o contador
# [ ] Imprime de 10 ate 0 (incluindo o 0)
# [ ] Imprime "foguete!" ao final
#
# DICA
# ----
# Enquanto o contador for >= 0, imprima e decremente:
#
#   n = 10
#   while n >= 0:
#       print(n)
#       n -= 1
#   print("foguete!")
#
# VALIDACAO
# ---------
# A saida tem 11 numeros (10..0) seguidos de "foguete!".
# =============================================================================


# >>> SEU CODIGO AQUI <<<
