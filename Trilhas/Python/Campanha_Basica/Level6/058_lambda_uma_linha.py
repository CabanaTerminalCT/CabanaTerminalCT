# =============================================================================
# 058 - Lambda: uma linha
# Nivel: 4 estrelas
# Conceitos: lambda
# =============================================================================
#
# HISTORIA
# --------
# As vezes a CabanaTerminal so precisa de uma funcaozinha descartavel - dobrar
# um numero, dizer se e par. Pra isso existe a lambda: uma funcao anonima de
# uma linha so.
#
# TAREFA
# ------
# 1. Crie uma lambda dobro que multiplica por 2 e teste
# 2. Crie uma lambda eh_par que retorna True/False e teste
# 3. Use uma lambda dentro de sorted() pra ordenar uma lista de tuplas pelo
#    segundo item
#
# Exemplo de execucao:
#
#   $ python3 058_lambda_uma_linha.py
#   Dobro: 10
#   4 e par? True
#   5 e par? False
#   Ordenado por pontos: [('ana', 10), ('carla', 15), ('bruno', 20)]
#
# REQUISITOS
# ----------
# [ ] Cria lambdas com nome (dobro = lambda x: ...)
# [ ] Usa lambda como argumento de sorted com key
#
# DICA
# ----
# lambda x: x * 2 e equivalente a def f(x): return x * 2, so que numa linha.
# Com sorted: sorted(lista, key=lambda item: item[1]).
#
# VALIDACAO
# ---------
# dobro(5) -> 10; a lista de tuplas sai ordenada pelos pontos.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
