# =============================================================================
# 019 - Piramide de asteriscos
# Nivel: 4 estrelas
# Conceitos: for aninhado
# =============================================================================
#
# HISTORIA
# --------
# O banner ASCII da CabanaTerminal tem uma piramide desenhada a mao. Voce vai
# gerar a sua propria, de qualquer altura, usando um for dentro do outro. E o
# primeiro contato com loops aninhados - onde a coisa comeca a ficar bonita.
#
# TAREFA
# ------
# 1. Peca a altura N ao usuario
# 2. Desenhe uma piramide de asteriscos com N linhas, centralizada
#
# Exemplo de execucao (N = 4):
#
#   $ python3 019_piramide_asteriscos.py
#   Altura: 4
#      *
#     ***
#    *****
#   *******
#
# REQUISITOS
# ----------
# [ ] Usa dois loops for (aninhados)
# [ ] Cada linha tem espacos + asteriscos
# [ ] A piramide fica centralizada
#
# DICA
# ----
# Na linha i (comecando em 1), a quantidade de asteriscos e 2*i - 1 e de
# espacos e N - i. Voce pode montar a linha com multiplicacao de string:
#
#   for i in range(1, n + 1):
#       espacos = " " * (n - i)
#       estrelas = "*" * (2 * i - 1)
#       print(espacos + estrelas)
#
# O for aninhado entra se voce quiser desenhar caractere por caractere - as
# duas abordagens valem.
#
# VALIDACAO
# ---------
# N = 1 -> uma estrela. N = 4 -> 4 linhas com 1, 3, 5 e 7 estrelas.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
