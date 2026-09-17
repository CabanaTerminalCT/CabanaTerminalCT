# =============================================================================
# 048 - Operacoes de conjunto
# Nivel: 4 estrelas
# Conceitos: union, intersection, difference
# =============================================================================
#
# HISTORIA
# --------
# Dois times da CabanaTerminal resolveram desafios diferentes. Quem participou
# dos dois? Quem so do primeiro? Quem apareceu em pelo menos um? Tudo isso sai
# das operacoes de conjunto.
#
# TAREFA
# ------
# 1. Crie dois sets: time_a e time_b
# 2. Mostre a uniao (quem aparece em qualquer um)
# 3. Mostre a interseccao (quem aparece nos dois)
# 4. Mostre a diferenca (so no time_a)
#
# Exemplo de execucao:
#
#   $ python3 048_operacoes_de_conjunto.py
#   Uniao: {'ana', 'bruno', 'carla', 'duda'}
#   Interseccao: {'bruno', 'carla'}
#   So no time_a: {'ana'}
#
# REQUISITOS
# ----------
# [ ] Usa | ou .union()
# [ ] Usa & ou .intersection()
# [ ] Usa - ou .difference()
#
# DICA
# ----
# Os operadores matematicos funcionam direto em sets:
#   a | b  uniao
#   a & b  interseccao
#   a - b  diferenca
#
# VALIDACAO
# ---------
# Com time_a = {ana, bruno, carla} e time_b = {bruno, carla, duda}:
# uniao com 4 nomes, interseccao {bruno, carla}, diferenca {ana}.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
