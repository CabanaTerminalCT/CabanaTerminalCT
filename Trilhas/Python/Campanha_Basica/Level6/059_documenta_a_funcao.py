# =============================================================================
# 059 - Documenta a funcao
# Nivel: 3 estrelas
# Conceitos: docstring
# =============================================================================
#
# HISTORIA
# --------
# Codigo sem documentacao na CabanaTerminal e codigo que ninguem quer manter.
# Uma docstring explica o que a funcao faz, o que recebe e o que devolve - e
# o Python mostra ela no help().
#
# TAREFA
# ------
# 1. Defina uma funcao media(a, b) com docstring explicando parametros e
#    retorno
# 2. Defina uma funcao fatorial(n) com docstring
# 3. Use help() ou .__doc__ pra imprimir a documentacao de uma delas
#
# Exemplo de execucao:
#
#   $ python3 059_documenta_a_funcao.py
#   Media: 7.5
#   Documentacao:
#   Calcula a media de dois numeros.
#   ...
#
# REQUISITOS
# ----------
# [ ] Usa docstring (texto entre tres aspas logo apos o def)
# [ ] Documenta parametros e retorno
# [ ] Mostra a docstring com help() ou .__doc__
#
# DICA
# ----
# A docstring fica entre """...""" na primeira linha do corpo da funcao:
#
#   def media(a, b):
#       """Calcula a media de dois numeros."""
#       return (a + b) / 2
#
# VALIDACAO
# ---------
# media(7,8) -> 7.5 e a docstring aparece ao consultar help/media.__doc__.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
