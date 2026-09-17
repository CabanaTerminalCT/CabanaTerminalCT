# =============================================================================
# 065 - Sempre no final
# Nivel: 3 estrelas
# Conceitos: finally
# =============================================================================
#
# HISTORIA
# --------
# Algumas coisas na CabanaTerminal precisam acontecer SEMPRE, der erro ou nao:
# fechar conexao, liberar recurso, imprimir "sessao encerrada". O finally
# garante isso.
#
# TAREFA
# ------
# 1. Peca um numero
# 2. Tente converter e dividir 100 por ele
# 3. Trate o ValueError e o ZeroDivisionError
# 4. No finally, imprima "Sessao encerrada." - deve aparecer em TODOS os casos
#
# Exemplo de execucao:
#
#   $ python3 065_sempre_no_final.py
#   Numero: 4
#   Resultado: 25.0
#   Sessao encerrada.
#
#   $ python3 065_sempre_no_final.py
#   Numero: 0
#   Nao da pra dividir por zero.
#   Sessao encerrada.
#
# REQUISITOS
# ----------
# [ ] Usa finally
# [ ] O finally aparece nos dois cenarios (sucesso e erro)
# [ ] Trata os dois tipos de erro
#
# DICA
# ----
# finally roda depois do try e do except, independente do que aconteceu - ate
# se houver return. E o lugar do "faxina sempre".
#
# VALIDACAO
# ---------
# Com 4 -> resultado 25.0 e "Sessao encerrada."; com 0 -> erro e "Sessao
# encerrada." tambem.
# =============================================================================


# >>> SEU CODIGO AQUI <<<
