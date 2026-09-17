# =============================================================================
# 096 - Sobrescreve metodo
# Nivel: 4 estrelas
# Conceitos: override
# =============================================================================
#
# HISTORIA
# --------
# Mentor da CabanaTerminal se apresenta diferente de um membro comum: ele
# menciona a especialidade. Override permite redefinir o metodo apresentar() na
# classe filha mantendo o mesmo nome.
#
# TAREFA
# ------
# 1. Reuse Membro (com apresentar) e Mentor(Membro)
# 2. Na classe Mentor, redefina apresentar() pra incluir a especialidade
# 3. Crie um Membro e um Mentor e chame apresentar() nos dois
# 4. Mostre que cada um usa a sua versao
#
# Exemplo de execucao:
#
#   $ python3 096_sobrescreve_metodo.py
#   Sou ana, 30 pontos.
#   Sou bruno, mentor de seguranca.
#
# REQUISITOS
# ----------
# [ ] Redefine o metodo com o MESMO nome na filha
# [ ] Membro usa uma versao, Mentor usa outra
# [ ] (Bonus) chama super().apresentar() dentro da versao da filha
#
# DICA
# ----
# Python procura o metodo primeiro na classe do objeto; se achar na filha, usa
# a dela. Pra reaproveitar a versao da mae, chame super().apresentar().
#
# VALIDACAO
# ---------
# Cada objeto imprime a sua versao de apresentar().
# =============================================================================


# >>> SEU CODIGO AQUI <<<
