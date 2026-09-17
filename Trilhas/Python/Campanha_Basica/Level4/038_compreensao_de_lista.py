# =============================================================================
# 038 - Compreensao de lista
# Nivel: 4 estrelas
# Conceitos: list comprehension
# =============================================================================
#
# HISTORIA
# --------
# A galera da CabanaTerminal vive transformando lista: pega os pontos e
# multiplica, filtra os pares, deixa tudo em maiuscula. List comprehension faz
# isso numa linha so, do jeito pythonesco.
#
# TAREFA
# ------
# 1. Crie uma lista de numeros de 1 a 10
# 2. Crie uma nova lista com o dobro de cada numero (comprehension)
# 3. Crie uma lista so com os pares (comprehension com if)
# 4. Crie uma lista com os quadrados dos impares
#
# Exemplo de execucao:
#
#   $ python3 038_compreensao_de_lista.py
#   Dobro: [2, 4, 6, ..., 20]
#   Pares: [2, 4, 6, 8, 10]
#   Quadrados dos impares: [1, 9, 25, 49, 81]
#
# REQUISITOS
# ----------
# [ ] Usa pelo menos uma comprehension simples [expr for x in lista]
# [ ] Usa uma comprehension com filtro [expr for x in lista if cond]
#
# DICA
# ----
# O formato e: [expressao for item in sequencia if condicao]
#
#   dobro = [n * 2 for n in numeros]
#   pares = [n for n in numeros if n % 2 == 0]
#
# Equivale a um for com .append(), mas cabe numa linha.
#
# VALIDACAO
# ---------
# De 1 a 10: dobro vai a 20; pares [2,4,6,8,10]; quadrados dos impares
# [1,9,25,49,81].
# =============================================================================


# >>> SEU CODIGO AQUI <<<
