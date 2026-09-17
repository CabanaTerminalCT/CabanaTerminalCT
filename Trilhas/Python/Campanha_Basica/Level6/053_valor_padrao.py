# =============================================================================
# 053 - Valor padrao
# Nivel: 3 estrelas
# Conceitos: default args
# =============================================================================
#
# HISTORIA
# --------
# Na CabanaTerminal quase todo mundo tem o cargo "membro". So uns poucos sao
# "mentor". Em vez de exigir o cargo sempre, a funcao pode ter um valor padrao.
#
# TAREFA
# ------
# 1. Defina apresentar(nome, cargo="membro") que imprime
#    "<nome> e <cargo> da CabanaTerminal."
# 2. Chame apresentar("ana") - deve usar o padrao
# 3. Chame apresentar("dudu", "mentor") - deve sobrescrever
# 4. Defina uma funcao potencia(base, expoente=2) e teste com 1 e 2 argumentos
#
# Exemplo de execucao:
#
#   $ python3 053_valor_padrao.py
#   ana e membro da CabanaTerminal.
#   dudu e mentor da CabanaTerminal.
#   potencia(5) = 25
#   potencia(2, 3) = 8
#
# REQUISITOS
# ----------
# [ ] Pelo menos uma funcao com valor padrao
# [ ] Chama usando o padrao e sobrescrevendo
#
# DICA
# ----
# O parametro com padrao vai depois dos obrigatorios: def f(a, b=1). Se voce
# passar o segundo argumento, ele substitui o padrao.
#
# VALIDACAO
# ---------
# apresentar("ana") usa "membro"; potencia(5) -> 25; potencia(2,3) -> 8.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
