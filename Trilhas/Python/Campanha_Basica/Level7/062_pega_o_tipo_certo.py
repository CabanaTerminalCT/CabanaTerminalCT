# =============================================================================
# 062 - Pega o tipo certo
# Nivel: 3 estrelas
# Conceitos: except especifico
# =============================================================================
#
# HISTORIA
# --------
# Pegar "qualquer erro" no except e preguiça perigosa. Na CabanaTerminal a
# gente trata cada tipo: ValueError pra conversao, ZeroDivisionError pra
# divisao por zero. Assim o programa reage certo a cada problema.
#
# TAREFA
# ------
# 1. Peca dois numeros e divida um pelo outro
# 2. Trate ValueError se a entrada nao for numero
# 3. Trate ZeroDivisionError se o divisor for zero
# 4. Cada except com sua mensagem especifica
#
# Exemplo de execucao:
#
#   $ python3 062_pega_o_tipo_certo.py
#   Numero 1: 10
#   Numero 2: 0
#   Nao da pra dividir por zero!
#
#   $ python3 062_pega_o_tipo_certo.py
#   Numero 1: abc
#   Isso nao e um numero!
#
# REQUISITOS
# ----------
# [ ] Usa dois except diferentes
# [ ] Um pra ValueError, outro pra ZeroDivisionError
# [ ] Mensagens especificas pra cada caso
#
# DICA
# ----
# Cada except declara o tipo:
#
#   except ValueError:
#       ...
#   except ZeroDivisionError:
#       ...
#
# VALIDACAO
# ---------
# "abc" -> erro de valor; divisor 0 -> erro de divisao por zero.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
