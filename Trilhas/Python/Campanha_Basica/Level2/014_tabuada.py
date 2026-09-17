# =============================================================================
# 014 - Tabuada
# Nivel: 2 estrelas
# Conceitos: for + range
# =============================================================================
#
# HISTORIA
# --------
# Na lousa da CabanaTerminal tem uma tabuada velha escrita a mao. A gente vai
# gerar todas elas automaticamente. Escolhe um numero e o computador cospe a
# tabuada de 1 a 10.
#
# TAREFA
# ------
# 1. Peca um numero inteiro ao usuario
# 2. Imprima a tabuada desse numero de 1 ate 10, no formato "n x i = resultado"
#
# Exemplo de execucao:
#
#   $ python3 014_tabuada.py
#   Numero: 7
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 10 = 70
#
# REQUISITOS
# ----------
# [ ] Usa for com range
# [ ] Converte a entrada com int()
# [ ] Imprime as 10 linhas, de 1 a 10
# [ ] O formato bate com o exemplo
#
# DICA
# ----
# range(1, 11) gera de 1 ate 10 (o 11 fica de fora). Use f-string pra montar
# a linha:
#
#   for i in range(1, 11):
#       print(f"{n} x {i} = {n * i}")
#
# VALIDACAO
# ---------
# Numero 7 -> ultima linha "7 x 10 = 70".
# =============================================================================


# >>> SEU CODIGO AQUI <<<
