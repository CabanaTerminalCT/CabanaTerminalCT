# =============================================================================
# 097 - Metodo magico
# Nivel: 4 estrelas
# Conceitos: __str__, __repr__
# =============================================================================
#
# HISTORIA
# --------
# Quando voce da print num objeto da CabanaTerminal, aparece algo feio tipo
# <Membro object at 0x...>. Os metodos magicos __str__ e __repr__ ensinam o
# Python a mostrar o objeto do jeito que a gente quer.
#
# TAREFA
# ------
# 1. Crie Membro com nome e pontos
# 2. Defina __str__ pra devolver algo legivel como "Membro: ana (30 pontos)"
# 3. Defina __repr__ pra devolver algo tecnico tipo "Membro('ana', 30)"
# 4. Use print(), str() e repr() pra ver a diferenca
#
# Exemplo de execucao:
#
#   $ python3 097_metodo_magico.py
#   print: Membro: ana (30 pontos)
#   str:   Membro: ana (30 pontos)
#   repr:  Membro('ana', 30)
#
# REQUISITOS
# ----------
# [ ] Define __str__
# [ ] Define __repr__
# [ ] Mostra a diferenca entre print/str e repr
#
# DICA
# ----
# __str__ e a versao "amigavel" (pro usuario). __repr__ e a "tecnica", ideal
# pra debugar, de preferencia algo que poderia recriar o objeto.
#
# VALIDACAO
# ---------
# print e str usam __str__; repr() e a lista no console usam __repr__.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
