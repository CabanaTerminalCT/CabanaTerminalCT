# =============================================================================
# 037 - Lista dentro de lista
# Nivel: 3 estrelas
# Conceitos: matriz simples
# =============================================================================
#
# HISTORIA
# --------
# O placar da CabanaTerminal tem linhas (times) e colunas (rodadas). Isso e
# uma matriz: uma lista onde cada item e outra lista. Percorrer isso exige
# dois loops aninhados.
#
# TAREFA
# ------
# 1. Crie uma matriz 2x3 (2 linhas, 3 colunas) com numeros
# 2. Imprima a matriz inteira
# 3. Imprima o elemento da linha 1, coluna 2 (lembre: indices do zero)
# 4. Percorra a matriz com dois fors e imprima cada valor
#
# Exemplo de execucao:
#
#   $ python3 037_lista_dentro_de_lista.py
#   Matriz: [[1, 2, 3], [4, 5, 6]]
#   Elemento [1][2]: 6
#   Valores:
#   1
#   2
#   ...
#   6
#
# REQUISITOS
# ----------
# [ ] Cria a matriz como lista de listas
# [ ] Acessa com dois indices matriz[l][c]
# [ ] Percorre com for dentro de for
#
# DICA
# ----
# matriz[1][2] pega a linha 1 e a coluna 2. Pra percorrer:
#
#   for linha in matriz:
#       for valor in linha:
#           print(valor)
#
# VALIDACAO
# ---------
# [[1,2,3],[4,5,6]] -> elemento [1][2] e 6; percorrer mostra 1..6.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
