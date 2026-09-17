# =============================================================================
# 015 - Soma acumulada
# Nivel: 3 estrelas
# Conceitos: for + acumulador
# =============================================================================
#
# HISTORIA
# --------
# O placar da CabanaTerminal soma ponto por ponto durante um mutirao. Voce vai
# fazer o mesmo: somar todos os numeros de 1 ate N usando um acumulador. Esse
# padrao aparece em toda analise de dados.
#
# TAREFA
# ------
# 1. Peca um numero N ao usuario
# 2. Some todos os inteiros de 1 ate N (inclusive)
# 3. Mostre o total
#
# Exemplo de execucao:
#
#   $ python3 015_soma_acumulada.py
#   Somar de 1 ate: 5
#   Total: 15
#
# (1 + 2 + 3 + 4 + 5 = 15)
#
# REQUISITOS
# ----------
# [ ] Usa for com range
# [ ] Usa uma variavel acumuladora iniciada em 0
# [ ] Soma cada valor dentro do loop
# [ ] Mostra o total so no final
#
# DICA
# ----
# O acumulador precisa existir FORA do loop e ser atualizado DENTRO:
#
#   total = 0
#   for i in range(1, n + 1):
#       total += i
#   print(f"Total: {total}")
#
# VALIDACAO
# ---------
# N = 5 -> 15. N = 10 -> 55. N = 1 -> 1. N = 0 -> 0.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
