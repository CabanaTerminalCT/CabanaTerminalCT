# =============================================================================
# 063 - Guarda o erro
# Nivel: 3 estrelas
# Conceitos: except ... as e
# =============================================================================
#
# HISTORIA
# --------
# Quando algo quebra na CabanaTerminal, a gente quer saber exatamente o que
# aconteceu pra logar. O "as" captura o objeto do erro, com a mensagem
# original do Python.
#
# TAREFA
# ------
# 1. Peca um numero e converta pra inteiro
# 2. No except, capture o erro com "as e"
# 3. Imprima a mensagem do erro junto com a sua
# 4. Imprima tambem o tipo do erro com type(e)
#
# Exemplo de execucao:
#
#   $ python3 063_guarda_o_erro.py
#   Numero: abc
#   Falhou: invalid literal for int() with base 10: 'abc'
#   Tipo: <class 'ValueError'>
#
# REQUISITOS
# ----------
# [ ] Usa except ... as e
# [ ] Imprime a mensagem do erro
# [ ] Imprime o tipo do erro
#
# DICA
# ----
# A variavel "e" guarda o objeto da excecao. str(e) da a mensagem e type(e) da
# a classe. Isso ajuda muito a debugar.
#
# VALIDACAO
# ---------
# Com "abc" a saida mostra a mensagem original e <class 'ValueError'>.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
